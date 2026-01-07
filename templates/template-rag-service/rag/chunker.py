"""Document chunking module."""

from pathlib import Path
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class Chunk:
    """A document chunk."""
    text: str
    source: str
    chunk_id: int
    metadata: Dict = None


def load_document(filepath: Path) -> str:
    """Load a text document."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50
) -> List[str]:
    """Split text into overlapping chunks."""
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        # Try to break at sentence boundary
        if end < len(text):
            last_period = chunk.rfind(".")
            if last_period > chunk_size // 2:
                chunk = chunk[:last_period + 1]
                end = start + last_period + 1

        chunks.append(chunk.strip())
        start = end - overlap

    return chunks


def process_documents(directory: Path) -> List[Chunk]:
    """Process all documents in a directory."""
    all_chunks = []
    chunk_id = 0

    for filepath in directory.glob("*.txt"):
        content = load_document(filepath)
        text_chunks = chunk_text(content)

        for text in text_chunks:
            all_chunks.append(Chunk(
                text=text,
                source=filepath.name,
                chunk_id=chunk_id
            ))
            chunk_id += 1

    return all_chunks
