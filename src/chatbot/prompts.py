from langchain_core.prompts import ChatPromptTemplate


def get_rag_prompt() -> ChatPromptTemplate:
    """
    Create and return the RAG prompt template.
    """

    prompt = ChatPromptTemplate.from_template(
        """
You are a helpful AI assistant.

Answer the user's question ONLY using the provided context.

Instructions:
- Use only the information available in the context.
- If the answer is not present in the context, reply:
  "I couldn't find that information in the provided documents."
- Do not make up facts.
- Keep your answers clear, concise, and professional.

Context:
{context}

Question:
{question}

Answer:
"""
    )

    return prompt