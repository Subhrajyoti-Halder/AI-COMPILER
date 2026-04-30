from utils.llm import call_llm
from utils.parser import safe_json_parse
from schemas.final_schema import FinalSchema


def generate_final_schema(intent_data: dict, design_data: dict):
    """
    Stage 3:
    Generate executable schemas:
    UI + API + DB + Auth
    """

    prompt = f"""
You are generating strict production-ready software schemas.

Return STRICT valid JSON only.

Rules:
- No markdown
- No explanation
- JSON only

Required structure:

ui_pages:
- list of objects
- each object:
  - name
  - components (list)

api_endpoints:
- list of objects
- each object:
  - path
  - method
  - description

db_tables:
- list of objects
- each object:
  - name
  - fields (list)

auth_rules:
- dictionary
- role → permissions list

Intent:
{intent_data}

System Design:
{design_data}
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
        validated = FinalSchema(**parsed_json)

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