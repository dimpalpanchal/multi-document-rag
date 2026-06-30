# 📚 RAG Chatbot using LangChain, ChromaDB & Llama 3.3

A modular Retrieval-Augmented Generation (RAG) chatbot built using **LangChain (LCEL)**, **ChromaDB**, **HuggingFace Embeddings**, and **Llama 3.3 (Groq)**.

The chatbot indexes multiple PDF documents, retrieves the most relevant information using **Maximum Marginal Relevance (MMR)** retrieval, and generates grounded answers with source citations.

---

# 🚀 Features

- Multi-PDF ingestion
- Recursive text chunking
- HuggingFace embedding model
- ChromaDB vector database
- Maximum Marginal Relevance (MMR) retrieval
- LangChain LCEL pipeline
- Llama 3.3 via Groq API
- Source citations
- Configurable retrieval parameters
- Modular project architecture

---

# 📂 Supported Documents

The chatbot can retrieve information from multiple categories of PDFs:

- 📄 Research Papers
- 💼 Job Descriptions
- 👨‍💻 Resumes
- 📘 Technical Documentation

Current dataset contains:

- 15 PDF documents
- ~390 pages
- 1151 text chunks

---

# 🏗️ Project Architecture

```
                   PDFs
                     │
                     ▼
               PDF Loader
                     │
                     ▼
      Recursive Character Splitter
                     │
                     ▼
      HuggingFace Embeddings (BGE)
                     │
                     ▼
                ChromaDB
                     │
                     ▼
             MMR Retriever
                     │
                     ▼
            Relevant Chunks
                     │
                     ▼
             Prompt Template
                     │
                     ▼
          Llama 3.3 (Groq API)
                     │
                     ▼
         Final Answer + Sources
```

---

# 📁 Project Structure

```
rag_chatbot/

│
├── data/
│   ├── chroma_db/
│   └── pdfs/
│       ├── docs/
│       ├── jobs/
│       ├── research/
│       └── resumes/
│
├── src/
│   ├── chatbot/
│   ├── ingestion/
│   ├── retrieval/
│   ├── app.py
│   ├── config.py
│   ├── main.py
│   └── playground.py
│
├── requirements.txt
├── README.md
└── .env.example
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository_url>

cd rag_chatbot
```

Create virtual environment

```bash
python -m venv rag

rag\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY
```

---

# ▶️ Build Vector Database

After adding PDFs:

```bash
python src/main.py
```

Pipeline executed:

- Load PDFs
- Chunk Documents
- Generate Embeddings
- Store in ChromaDB

---

# 💬 Run Chatbot

```bash
python src/playground.py
```

Example:

```
Question:
What is self-attention?

Answer:
Self-attention is an attention mechanism relating different positions within a sequence to compute contextual representations.

Sources:
Attention Is All You Need.pdf
Page 2
```

---

# ⚙️ Configuration

The project is configurable from `config.py`.

Example settings:

```python
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150

TOP_K_RESULTS = 4

SEARCH_TYPE = "mmr"

FETCH_K_RESULTS = 10

DEBUG_MODE = False

SHOW_SOURCES = True
```

---

# 🔍 Retrieval Strategy

Initially the project used **Similarity Search**.

During testing, duplicate chunks were frequently retrieved.

Example:

```
Chunk 1

Chunk 2 (duplicate)

Chunk 3

Chunk 4 (duplicate)
```

This reduced retrieval diversity and negatively affected answer quality.

The retriever was updated to **Maximum Marginal Relevance (MMR)**.

Benefits:

- More diverse retrieval
- Better context coverage
- Reduced duplicate chunks
- Improved answer quality

---

# 💡 Challenges Faced

## 1. Duplicate Retrieval

Problem:

Similarity search returned repeated chunks from the same document.

Solution:

Switched to MMR retrieval.

---

## 2. LangChain API Changes

The project was built using **LangChain 1.x**.

Many tutorials online still use deprecated APIs such as:

- `create_retrieval_chain`
- `ConversationBufferMemory`
- `langchain.chains`

The project was updated to use modern LCEL-based composition.

---

## 3. Chroma Deprecation

Originally:

```python
from langchain_community.vectorstores import Chroma
```

Updated to:

```python
from langchain_chroma import Chroma
```

---

## 4. Python Import Issues

Running scripts inside nested folders caused:

```
ModuleNotFoundError
```

The project structure was reorganized to simplify imports.

---

## 5. Prompt Engineering

The chatbot prompt was refined to:

- Answer only using retrieved context
- Avoid hallucinations
- Return "I couldn't find that information..." when context is insufficient

---

# 🛠️ Technologies Used

- Python
- LangChain (LCEL)
- HuggingFace Embeddings
- ChromaDB
- Groq API
- Llama 3.3
- RecursiveCharacterTextSplitter
- dotenv

---

# 📈 Future Improvements

- Conversational Memory
- History-Aware Retrieval
- RAG Evaluation (Ragas)
- DeepEval Integration
- Streaming Responses
- Web Interface (Streamlit)

---

# 📚 Key Learnings

During this project I learned:

- Retrieval-Augmented Generation (RAG) pipeline
- Vector databases
- Semantic search
- Embedding models
- Prompt engineering
- MMR retrieval
- LangChain LCEL
- ChromaDB indexing
- Modular project design
- Debugging modern LangChain APIs

---

# 🙏 Acknowledgements

This project was developed as part of my learning journey into Retrieval-Augmented Generation (RAG), LangChain, vector databases, and LLM application development.

The goal was not only to build a working chatbot but also to understand the complete RAG pipeline—from document ingestion and embedding generation to retrieval optimization and grounded response generation.