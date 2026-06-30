from app import load_app

from chatbot.chain import format_docs

from config import (
    DEBUG_MODE,
    SHOW_SOURCES,
)


def main():

    app = load_app()

    retriever = app["retriever"]

    rag_chain = app["rag_chain"]

    print("\nChatbot Ready!")

    while True:

        print("\n" + "=" * 70)

        query = input("Ask a question (or type 'exit'): ")

        if query.lower() == "exit":
            print("\nGoodbye!")
            break

        # --------------------------------------------------
        # Retrieve Documents
        # --------------------------------------------------

        documents = retriever.invoke(query)

        context = format_docs(documents)

        # --------------------------------------------------
        # Debug Mode
        # --------------------------------------------------

        if DEBUG_MODE:

            print("\n" + "=" * 70)
            print("Retrieved Documents")
            print("=" * 70)

            for i, doc in enumerate(documents, start=1):

                print(f"\n----- DOCUMENT {i} -----\n")

                print(doc.page_content)

        # --------------------------------------------------
        # Generate Answer
        # --------------------------------------------------

        answer = rag_chain.invoke(
            {
                "context": context,
                "question": query,
            }
        )

        print("\n" + "=" * 70)
        print("Answer")
        print("=" * 70)

        print(answer)

        # --------------------------------------------------
        # Source Citations
        # --------------------------------------------------

        if SHOW_SOURCES:

            print("\n" + "=" * 70)
            print("Sources")
            print("=" * 70)

            for i, doc in enumerate(documents, start=1):

                print(f"\n[{i}]")

                print(f"Source   : {doc.metadata['source']}")
                print(f"Category : {doc.metadata['category']}")
                print(f"Page     : {doc.metadata['page'] + 1}")


if __name__ == "__main__":
    main()