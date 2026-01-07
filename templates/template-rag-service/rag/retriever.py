"""Document retrieval module."""

from typing import List
from dataclasses import dataclass
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from rag.chunker import Chunk


@dataclass
class SearchResult:
    """A search result."""
    chunk: Chunk
    score: float


class TFIDFRetriever:
    """Simple TF-IDF based retriever."""

    def __init__(self):
        self.vectorizer = TfidfVectorizer()
        self.chunks: List[Chunk] = []
        self.vectors = None

    def index(self, chunks: List[Chunk]) -> None:
        """Index document chunks."""
        self.chunks = chunks
        texts = [c.text for c in chunks]
        self.vectors = self.vectorizer.fit_transform(texts)

    def search(self, query: str, top_k: int = 3) -> List[SearchResult]:
        """Search for relevant chunks."""
        if self.vectors is None:
            return []

        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.vectors)[0]

        # Get top-k indices
        top_indices = np.argsort(similarities)[-top_k:][::-1]

        results = []
        for idx in top_indices:
            if similarities[idx] > 0:
                results.append(SearchResult(
                    chunk=self.chunks[idx],
                    score=float(similarities[idx])
                ))

        return results

    def save(self, filepath: str) -> None:
        """Save the index."""
        import pickle
        with open(filepath, "wb") as f:
            pickle.dump({
                "chunks": self.chunks,
                "vectorizer": self.vectorizer,
                "vectors": self.vectors
            }, f)

    def load(self, filepath: str) -> None:
        """Load the index."""
        import pickle
        with open(filepath, "rb") as f:
            data = pickle.load(f)
            self.chunks = data["chunks"]
            self.vectorizer = data["vectorizer"]
            self.vectors = data["vectors"]
