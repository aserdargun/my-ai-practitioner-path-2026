# Skill: Build RAG

Build a Retrieval-Augmented Generation system.

## When to Use

- Building Q&A over documents
- Creating knowledge-base chatbots
- Augmenting LLMs with custom data

## Playbook

### Phase 1: Document Preparation (30 min)

```python
# Load and chunk documents
from pathlib import Path

def load_documents(directory):
    """Load text files from directory."""
    docs = []
    for file in Path(directory).glob('*.txt'):
        with open(file) as f:
            docs.append({
                'content': f.read(),
                'source': file.name
            })
    return docs

def chunk_text(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks

# Process documents
docs = load_documents('data/')
all_chunks = []
for doc in docs:
    chunks = chunk_text(doc['content'])
    for i, chunk in enumerate(chunks):
        all_chunks.append({
            'text': chunk,
            'source': doc['source'],
            'chunk_id': i
        })
```

### Phase 2: Embedding and Indexing (30 min)

```python
# Simple TF-IDF approach (no external APIs needed)
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class SimpleRetriever:
    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.chunks = []
        self.vectors = None

    def index(self, chunks):
        """Index document chunks."""
        self.chunks = chunks
        texts = [c['text'] for c in chunks]
        self.vectors = self.vectorizer.fit_transform(texts)

    def search(self, query, top_k=3):
        """Search for relevant chunks."""
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.vectors)[0]
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        results = []
        for idx in top_indices:
            results.append({
                'chunk': self.chunks[idx],
                'score': similarities[idx]
            })
        return results

# Build index
retriever = SimpleRetriever()
retriever.index(all_chunks)
```

### Phase 3: Query Pipeline (30 min)

```python
def build_prompt(query, context_chunks):
    """Build prompt with retrieved context."""
    context = "\n\n".join([c['chunk']['text'] for c in context_chunks])

    prompt = f"""Answer the question based on the following context.
If the answer is not in the context, say "I don't have enough information."

Context:
{context}

Question: {query}

Answer:"""
    return prompt

def rag_query(query, retriever):
    """Full RAG pipeline."""
    # Retrieve relevant chunks
    results = retriever.search(query, top_k=3)

    # Build prompt
    prompt = build_prompt(query, results)

    # Return prompt (would send to LLM in production)
    return {
        'prompt': prompt,
        'sources': [r['chunk']['source'] for r in results]
    }
```

### Phase 4: Evaluation (30 min)

```python
# Test queries
test_queries = [
    "What is the main topic?",
    "How does X work?",
    "What are the key points?"
]

for query in test_queries:
    result = rag_query(query, retriever)
    print(f"Query: {query}")
    print(f"Sources: {result['sources']}")
    print("---")
```

## Deliverables

- [ ] Document chunking pipeline
- [ ] Retrieval system (TF-IDF or embeddings)
- [ ] Query pipeline
- [ ] Evaluation with test queries
- [ ] Documentation

## Tips

- Start with TF-IDF before moving to embeddings
- Chunk size affects retrieval quality
- Always cite sources
- Test with diverse queries
