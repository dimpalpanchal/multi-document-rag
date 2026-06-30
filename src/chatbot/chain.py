from langchain_core.output_parsers import StrOutputParser


def format_docs(documents):
    """
    Convert retrieved documents into a single context string.
    """

    return "\n\n".join(
        doc.page_content for doc in documents
    )


def create_rag_chain(
    llm,
    prompt,
):
    """
    Create a simple LCEL chain.

    Input:
        {
            "context": "...",
            "question": "..."
        }

    Output:
        Answer string.
    """

    rag_chain = (

        prompt

        | llm

        | StrOutputParser()

    )

    return rag_chain