from utils.llm import call_llm
from utils.parser import safe_json_parse
from schemas.intent_schema import IntentSchema


def extract_intent(user_prompt: str):
    """
    Stage 1:
    Convert raw natural language prompt
    into structured intent JSON
    """

    prompt = f"""
Extract the software requirements from the following user request.

Return STRICT valid JSON only.

Rules:
- No markdown
- No explanation
- JSON only
- monetization must be a list
- integrations must be a list

Required fields:
- app_type (string)
- features (list)
- roles (list)
- monetization (list)
- integrations (list)

User Request:
{user_prompt}
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
        validated = IntentSchema(**parsed_json)

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