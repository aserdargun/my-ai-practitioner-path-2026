"""Report generation."""

from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from eval.runner import EvaluationResults


def generate_report(results: "EvaluationResults") -> str:
    """Generate a text report."""
    lines = [
        "=" * 50,
        "EVALUATION REPORT",
        "=" * 50,
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "SUMMARY",
        "-" * 50,
        f"Total Cases: {results.summary['total_cases']}",
        f"Correct: {results.summary['correct']}",
        f"Accuracy: {results.summary['accuracy']:.2%}",
        f"Avg Latency: {results.summary['average_latency_ms']:.2f}ms",
        "",
        "ACCURACY BY CATEGORY",
        "-" * 50,
    ]

    for cat, acc in results.summary["accuracy_by_category"].items():
        lines.append(f"  {cat}: {acc:.2%}")

    failures = results.get_failures()
    if failures:
        lines.extend([
            "",
            f"FAILURES ({len(failures)})",
            "-" * 50,
        ])
        for f in failures[:10]:  # Show first 10
            lines.append(f"  [{f.id}] Expected: {f.expected}, Got: {f.predicted}")
            lines.append(f"         Input: {f.input[:50]}...")

    lines.append("=" * 50)

    return "\n".join(lines)


def generate_json_report(results: "EvaluationResults") -> dict:
    """Generate a JSON-serializable report."""
    return {
        "timestamp": datetime.now().isoformat(),
        "summary": results.summary,
        "results": [
            {
                "id": r.id,
                "input": r.input,
                "expected": r.expected,
                "predicted": r.predicted,
                "correct": r.correct,
                "latency_ms": r.latency_ms,
                "category": r.category
            }
            for r in results.results
        ]
    }
