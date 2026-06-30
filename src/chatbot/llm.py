import os

from dotenv import load_dotenv

from langchain_groq import ChatGroq

from config import (
    LLAMA_MODEL,
    TEMPERATURE,
    MAX_TOKENS,
)


load_dotenv()


def get_llm() -> ChatGroq:
    """
    Load and return the Groq Llama model.

    Returns:
        ChatGroq instance.
    """

    groq_api_key = os.getenv("GROQ_API_KEY")

    if not groq_api_key:
        raise ValueError(
            "GROQ_API_KEY not found in .env file."
        )

    llm = ChatGroq(
        api_key=groq_api_key,
        model=LLAMA_MODEL,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
    )

    return llm