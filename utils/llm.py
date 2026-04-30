import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = os.getenv("MODEL_NAME")


def call_llm(prompt: str) -> str:
    """
    Generic reusable LLM caller
    Returns strict JSON output
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a strict software compiler system. "
                    "Always return valid JSON only. "
                    "No markdown. No explanations."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content