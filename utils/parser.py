import json
import re


def safe_json_parse(text: str):
    """
    Safely parse JSON from LLM output.
    Handles:
    - markdown code fences
    - extra text before/after JSON
    - formatting noise
    """

    try:
        # Remove markdown fences like ```json ... ```
        text = text.strip()
        text = re.sub(r"```json", "", text)
        text = re.sub(r"```", "", text)

        # Extract first JSON object
        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:
            text = text[start:end + 1]

        parsed = json.loads(text)
        return parsed, None

    except Exception as e:
        return None, str(e)