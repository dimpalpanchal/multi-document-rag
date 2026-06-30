from ingestion.embedder import get_embedding_model

from retrieval.vectorstore import load_vector_store
from retrieval.retriever import create_retriever

from chatbot.llm import get_llm
from chatbot.prompts import get_rag_prompt
from chatbot.chain import create_rag_chain


def load_app():

    print("=" * 70)
    print("Loading Embedding Model...")
    print("=" * 70)

    embedding_model = get_embedding_model()

    print("✓ Embedding Model Loaded")

    print("\nLoading Chroma Database...")

    vector_store = load_vector_store(embedding_model)

    print("✓ Vector Database Loaded")

    print("\nCreating Retriever...")

    retriever = create_retriever(vector_store)

    print("✓ Retriever Ready")

    print("\nLoading Llama...")

    llm = get_llm()

    print("✓ Llama Loaded Successfully!")

    print("\nLoading Prompt...")

    prompt = get_rag_prompt()

    print("✓ Prompt Ready")

    print("\nCreating RAG Chain...")

    rag_chain = create_rag_chain(
        llm=llm,
        prompt=prompt,
    )

    print("✓ RAG Chain Ready")

    return {
        "retriever": retriever,
        "rag_chain": rag_chain,
    }