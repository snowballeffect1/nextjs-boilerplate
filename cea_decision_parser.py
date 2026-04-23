import json
import re
from typing import Dict, Any, Optional

class CEADecisionParser:
    """Parser for CEA (Comisión de Energía Atómica) decisions."""

    def __init__(self, original: str, cea: str):
        self.original = original
        self.cea = cea

    def parse(self) -> Dict[str, Any]:
        """Parse the CEA decision and return structured data."""
        result = {
            "original": self.original,
            "cea": self.cea,
            "parsed": {}
        }

        # Extract key fields from CEA decision
        cea_data = json.loads(self.cea) if isinstance(self.cea, str) else self.cea
        original_data = json.loads(self.original) if isinstance(self.original, str) else self.original

        # Parse decision details
        result["parsed"] = self._extract_decision_details(cea_data, original_data)

        return result

    def _extract_decision_details(self, cea: Dict[str, Any], original: Dict[str, Any]) -> Dict[str, Any]:
        """Extract structured details from CEA decision."""
        details = {}

        # Decision ID
        details["decision_id"] = cea.get("decision_id", original.get("id", ""))

        # Date
        details["date"] = cea.get("date", original.get("fecha", ""))

        # Subject
        details["subject"] = cea.get("subject", original.get("asunto", ""))

        # Decision type
        details["decision_type"] = cea.get("type", original.get("tipo", ""))

        # Status
        details["status"] = cea.get("status", original.get("estado", ""))

        # Content
        details["content"] = cea.get("content", original.get("contenido", ""))

        # Additional metadata
        details["metadata"] = {
            "source": "CEA",
            "version": "1.0",
            "parsed_at": "2025-04-11T00:00:00Z"
        }

        return details

    def to_json(self) -> str:
        """Return parsed result as JSON string."""
        return json.dumps(self.parse(), ensure_ascii=False, indent=2)


def parse_cea_decision(original: str, cea: str) -> str:
    """Convenience function to parse CEA decision."""
    parser = CEADecisionParser(original, cea)
    return parser.to_json()
