from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import logging
from app.prompts import EXPLAIN_CODE_PROMPT

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def explain_code_with_llm(code: str, language: str):
    prompt = EXPLAIN_CODE_PROMPT.format(
        code=code,
        language=language or "unspecified"
    )

    logger.info(f"Whats the prompt: {prompt}")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a precise and strict JSON generator."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={ "type": "json_object" },
        temperature=0.1
    )

    content = response.choices[0].message.content
    logger.info(f"LLM Response: {content}")

    try:
        parsed = json.loads(content)
        logger.info(f"parsed json: {parsed}")
        return parsed
    except json.JSONDecodeError as e:
        logger.error(f"JSON Decode Error: {e}")  # Debug print
        logger.error(f"Content that failed: {content}")  # Debug print
        raise ValueError(f"LLM returned invalid JSON: {str(e)}")