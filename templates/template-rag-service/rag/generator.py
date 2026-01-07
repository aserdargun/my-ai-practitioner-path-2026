"""Response generation module."""

from typing import List
from dataclasses import dataclass

from rag.retriever import SearchResult


@dataclass
class GeneratedResponse:
    """A generated response."""
    answer: str
    sources: List[str]
    context_used: str


def build_prompt(query: str, results: List[SearchResult]) -> str:
    """Build a prompt with context."""
    context = "\n\n".join([r.chunk.text for r in results])

    prompt = f"""Answer the question based on the following context.
If the answer is not in the context, say "I don't have enough information."

Context:
{context}

Question: {query}

Answer:"""

    return prompt


def generate_response(
    query: str,
    results: List[SearchResult],
    llm_fn=None
) -> GeneratedResponse:
    """Generate a response using retrieved context."""
    if not results:
        return GeneratedResponse(
            answer="No relevant documents found.",
            sources=[],
            context_used=""
        )

    prompt = build_prompt(query, results)
    sources = list(set(r.chunk.source for r in results))
    context = "\n".join([r.chunk.text for r in results])

    # If an LLM function is provided, use it
    if llm_fn:
        answer = llm_fn(prompt)
    else:
        # Placeholder: return the context
        answer = f"Based on the documents ({', '.join(sources)}), the relevant context is:\n\n{context}"

    return GeneratedResponse(
        answer=answer,
        sources=sources,
        context_used=context
    )
