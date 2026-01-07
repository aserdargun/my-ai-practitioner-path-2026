# RAG Service Template

A template for Retrieval-Augmented Generation systems.

## Structure

```
template-rag-service/
├── rag/
│   ├── __init__.py
│   ├── chunker.py      # Document chunking
│   ├── retriever.py    # Search/retrieval
│   ├── generator.py    # Response generation
│   └── pipeline.py     # Full RAG pipeline
├── tests/
│   └── test_rag.py
├── data/
│   └── documents/      # Source documents
├── requirements.txt
└── README.md
```

## Quick Start

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Index documents
python -m rag.pipeline index data/documents/

# Query
python -m rag.pipeline query "What is the main topic?"
```

## Usage

```python
from rag.pipeline import RAGPipeline

# Initialize
rag = RAGPipeline()

# Index documents
rag.index_documents("data/documents/")

# Query
response = rag.query("What is X?")
print(response.answer)
print(response.sources)
```
