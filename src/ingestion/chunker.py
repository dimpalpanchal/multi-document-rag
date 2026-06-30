from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_SIZE, CHUNK_OVERLAP

def split_documents(documents: list[Document]) -> list[Document]:
    """
    Split LangChain documents into smaller chunks.

    Args:
        documents: List of loaded Document objects.

    Returns:
        List of chunked Document objects.
    """

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        add_start_index=True,
    )

    chunks = text_splitter.split_documents(documents)

    return chunks