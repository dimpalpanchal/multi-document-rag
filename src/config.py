"""
Project Configuration

This file contains all configurable parameters used across the project.
Changing values here updates the behavior everywhere they are imported.
"""

# ==========================================================
# Paths
# ==========================================================

PDF_DIRECTORY = "data/pdfs"

CHROMA_DB_DIRECTORY = "data/chroma_db"

# ==========================================================
# Chunking Configuration
# ==========================================================

CHUNK_SIZE = 800

CHUNK_OVERLAP = 150

# ==========================================================
# Embedding Model
# ==========================================================

EMBEDDING_MODEL_NAME = "BAAI/bge-small-en-v1.5"

EMBEDDING_DEVICE = "cpu"

NORMALIZE_EMBEDDINGS = True

# ==========================================================
# Retrieval Configuration
# (We'll use these later)
# ==========================================================

TOP_K_RESULTS = 4

FETCH_K_RESULTS = 10

# SEARCH_TYPE = "similarity"

SEARCH_TYPE = "mmr"

# ==========================================================
# LLM Configuration
# (We'll use these later)
# ==========================================================

LLAMA_MODEL = "llama-3.3-70b-versatile"

TEMPERATURE = 0.2

MAX_TOKENS = 1024

# ==========================================================
# Debug Configuration
# ==========================================================

DEBUG_MODE = False