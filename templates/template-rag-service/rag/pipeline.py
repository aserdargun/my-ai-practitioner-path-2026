"""Full RAG pipeline."""

import argparse
from pathlib import Path

from rag.chunker import process_documents
from rag.retriever import TFIDFRetriever
from rag.generator import generate_response, GeneratedResponse


class RAGPipeline:
    """Complete RAG pipeline."""

    def __init__(self):
        self.retriever = TFIDFRetriever()

    def index_documents(self, directory: str) -> int:
        """Index all documents in a directory."""
        path = Path(directory)
        chunks = process_documents(path)
        self.retriever.index(chunks)
        return len(chunks)

    def query(self, question: str, top_k: int = 3) -> GeneratedResponse:
        """Query the indexed documents."""
        results = self.retriever.search(question, top_k=top_k)
        return generate_response(question, results)

    def save_index(self, filepath: str) -> None:
        """Save the index to disk."""
        self.retriever.save(filepath)

    def load_index(self, filepath: str) -> None:
        """Load the index from disk."""
        self.retriever.load(filepath)


def main():
    parser = argparse.ArgumentParser(description="RAG Pipeline")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Index command
    index_parser = subparsers.add_parser("index", help="Index documents")
    index_parser.add_argument("directory", help="Document directory")
    index_parser.add_argument("--save", help="Save index to file")

    # Query command
    query_parser = subparsers.add_parser("query", help="Query documents")
    query_parser.add_argument("question", help="Question to ask")
    query_parser.add_argument("--index", help="Load index from file")
    query_parser.add_argument("--top-k", type=int, default=3)

    args = parser.parse_args()
    pipeline = RAGPipeline()

    if args.command == "index":
        count = pipeline.index_documents(args.directory)
        print(f"Indexed {count} chunks")
        if args.save:
            pipeline.save_index(args.save)
            print(f"Saved index to {args.save}")

    elif args.command == "query":
        if args.index:
            pipeline.load_index(args.index)

        response = pipeline.query(args.question, top_k=args.top_k)
        print(f"\nAnswer:\n{response.answer}")
        print(f"\nSources: {', '.join(response.sources)}")


if __name__ == "__main__":
    main()
