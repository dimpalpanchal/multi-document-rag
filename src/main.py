from config import PDF_DIRECTORY

from ingestion.loader import load_documents
from ingestion.chunker import split_documents
from ingestion.embedder import get_embedding_model

from retrieval.vectorstore import create_vector_store
from retrieval.retriever import create_retriever


def main():

    print("=" * 60)
    print("Loading PDF documents...")
    print("=" * 60)

    # Step 1
    documents = load_documents(PDF_DIRECTORY)

    # Step 2
    chunks = split_documents(documents)

    # Step 3
    embedding_model = get_embedding_model()

    print("\nEmbedding Model Loaded Successfully!")
    print(type(embedding_model))

    # Step 4
    vector_store = create_vector_store(
        chunks,
        embedding_model
    )

    print("\nVector Store Created Successfully!")

    # Step 5
    retriever = create_retriever(vector_store)

    print("Retriever Created Successfully!")

    print("\n" + "=" * 60)
    print("Pipeline Summary")
    print("=" * 60)

    print(f"Original Documents         : {len(documents)}")
    print(f"Total Chunks              : {len(chunks)}")
    print(f"Average Chunks/Document   : {len(chunks)/len(documents):.2f}")

    print("\nKnowledge Base Ready!")

if __name__ == "__main__":
    main()