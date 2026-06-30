from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.documents import Document


def load_documents(pdf_directory: str) -> list[Document]:
    """
    Load all PDFs recursively and enrich their metadata.

    Args:
        pdf_directory: Root directory containing PDFs.

    Returns:
        List of LangChain Document objects.
    """

    pdf_files = list(Path(pdf_directory).rglob("*.pdf"))

    documents: list[Document] = []

    print("=" * 60)
    print("Loading PDFs...")
    print("=" * 60)

    for pdf_file in pdf_files:

        try:
            loader = PyMuPDFLoader(str(pdf_file))
            docs = loader.load()

            category = pdf_file.parent.name

            for doc in docs:
                doc.metadata.update(
                    {
                        "source": pdf_file.name,
                        "category": category,
                    }
                )

            documents.extend(docs)

            print(f"✓ {pdf_file.name}")
            print(f"   Category : {category}")
            print(f"   Pages    : {len(docs)}\n")

        except Exception as e:
            print(f"✗ Failed to load {pdf_file.name}")
            print(f"  Error: {e}\n")

    print("-" * 60)
    print(f"PDFs Loaded : {len(pdf_files)}")
    print(f"Pages Loaded: {len(documents)}")
    print("-" * 60)

    return documents