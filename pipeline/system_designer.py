from utils.llm import call_llm
from utils.parser import safe_json_parse
from schemas.design_schema import DesignSchema


def generate_system_design(intent_data: dict):
    """
    Stage 2:
    Convert intent JSON into
    architecture-level design
    """

    prompt = f"""
You are designing software architecture.

Return STRICT valid JSON only.

Rules:
- No markdown
- No explanation
- JSON only

Required fields:

entities:
- list of strings

flows:
- list of objects
- each object must contain:
  - name
  - steps (list)

modules:
- list of objects
- each object must contain:
  - name
  - description

permissions:
- list of objects
- each object must contain:
  - role
  - permissions (list)

Intent:
{intent_data}
"""

    llm_output = call_llm(prompt)

    parsed_json, error = safe_json_parse(llm_output)

    if error:
        return {
            "success": False,
            "error": f"Invalid JSON from LLM: {error}",
            "raw_output": llm_output
        }

    try:
        validated = DesignSchema(**parsed_json)

        return {
            "success": True,
            "data": validated.dict()
        }

    except Exception as e:
        return {
            "success": False,
            "error": f"Schema validation failed: {str(e)}",
            "raw_output": parsed_json
        }