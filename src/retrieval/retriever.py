from langchain_chroma import Chroma

from config import (
    SEARCH_TYPE,
    TOP_K_RESULTS,
    FETCH_K_RESULTS,
)


def create_retriever(vector_store: Chroma):
    """
    Create a retriever from the Chroma vector store.

    Args:
        vector_store: Chroma vector database.

    Returns:
        LangChain Retriever.
    """

    search_kwargs = {
        "k": TOP_K_RESULTS,
    }

    # fetch_k is only valid for MMR search
    if SEARCH_TYPE == "mmr":
        search_kwargs["fetch_k"] = FETCH_K_RESULTS

    retriever = vector_store.as_retriever(
        search_type=SEARCH_TYPE,
        search_kwargs=search_kwargs,
    )

    return retriever