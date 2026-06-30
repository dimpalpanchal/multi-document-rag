from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config import CHROMA_DB_DIRECTORY


def create_vector_store(
    chunks: list[Document],
    embedding_model: HuggingFaceEmbeddings,
) -> Chroma:
    """
    Create and persist a Chroma vector database.

    Args:
        chunks: List of chunked documents.
        embedding_model: HuggingFace embedding model.

    Returns:
        Chroma vector store.
    """

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=CHROMA_DB_DIRECTORY,
    )

    return vector_store


def load_vector_store(
    embedding_model: HuggingFaceEmbeddings,
) -> Chroma:
    """
    Load an existing Chroma vector database.

    Args:
        embedding_model: HuggingFace embedding model.

    Returns:
        Chroma vector store.
    """

    vector_store = Chroma(
        persist_directory=CHROMA_DB_DIRECTORY,
        embedding_function=embedding_model,
    )

    return vector_store