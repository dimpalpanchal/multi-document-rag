from langchain_huggingface import HuggingFaceEmbeddings
from config import (
    EMBEDDING_MODEL_NAME,
    EMBEDDING_DEVICE,
    NORMALIZE_EMBEDDINGS,
)

def get_embedding_model() -> HuggingFaceEmbeddings:
    """
    Load and return the embedding model.

    Returns:
        HuggingFaceEmbeddings instance.
    """

    embedding_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL_NAME,
        model_kwargs={
            "device": EMBEDDING_DEVICE
        },
        encode_kwargs={
            "normalize_embeddings":  NORMALIZE_EMBEDDINGS,
        },
    )

    return embedding_model