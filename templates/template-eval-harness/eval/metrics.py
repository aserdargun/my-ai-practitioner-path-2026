"""Evaluation metrics."""

from typing import List, Dict
from dataclasses import dataclass


@dataclass
class EvalResult:
    """Result for a single test case."""
    id: str
    input: str
    expected: str
    predicted: str
    correct: bool
    latency_ms: float
    category: str


def accuracy(results: List[EvalResult]) -> float:
    """Calculate accuracy."""
    if not results:
        return 0.0
    correct = sum(1 for r in results if r.correct)
    return correct / len(results)


def accuracy_by_category(results: List[EvalResult]) -> Dict[str, float]:
    """Calculate accuracy per category."""
    categories = {}

    for r in results:
        if r.category not in categories:
            categories[r.category] = {"correct": 0, "total": 0}
        categories[r.category]["total"] += 1
        if r.correct:
            categories[r.category]["correct"] += 1

    return {
        cat: data["correct"] / data["total"]
        for cat, data in categories.items()
    }


def average_latency(results: List[EvalResult]) -> float:
    """Calculate average latency in ms."""
    if not results:
        return 0.0
    return sum(r.latency_ms for r in results) / len(results)


def failure_analysis(results: List[EvalResult]) -> List[EvalResult]:
    """Get all failed test cases."""
    return [r for r in results if not r.correct]


def summary_metrics(results: List[EvalResult]) -> Dict:
    """Generate summary metrics."""
    return {
        "total_cases": len(results),
        "correct": sum(1 for r in results if r.correct),
        "accuracy": accuracy(results),
        "accuracy_by_category": accuracy_by_category(results),
        "average_latency_ms": average_latency(results),
        "failures": len(failure_analysis(results))
    }
