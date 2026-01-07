"""Evaluation runner."""

import time
import argparse
from typing import Callable, List
from dataclasses import dataclass

from eval.dataset import load_dataset, TestCase
from eval.metrics import EvalResult, summary_metrics
from eval.report import generate_report


@dataclass
class EvaluationResults:
    """Complete evaluation results."""
    results: List[EvalResult]
    summary: dict

    def get_failures(self) -> List[EvalResult]:
        return [r for r in self.results if not r.correct]


class EvaluationRunner:
    """Run evaluations on a model."""

    def __init__(self, model_fn: Callable[[str], str]):
        self.model_fn = model_fn

    def run_single(self, test_case: TestCase) -> EvalResult:
        """Run evaluation on a single test case."""
        start = time.time()
        predicted = self.model_fn(test_case.input)
        latency = (time.time() - start) * 1000

        return EvalResult(
            id=test_case.id,
            input=test_case.input,
            expected=test_case.expected,
            predicted=predicted,
            correct=predicted == test_case.expected,
            latency_ms=latency,
            category=test_case.category
        )

    def evaluate(self, dataset_path: str) -> EvaluationResults:
        """Run evaluation on full dataset."""
        test_cases = load_dataset(dataset_path)
        results = []

        for tc in test_cases:
            result = self.run_single(tc)
            results.append(result)

        return EvaluationResults(
            results=results,
            summary=summary_metrics(results)
        )


def dummy_model(input_text: str) -> str:
    """Placeholder model for testing."""
    if "hello" in input_text.lower():
        return "positive"
    elif "bad" in input_text.lower():
        return "negative"
    return "neutral"


def main():
    parser = argparse.ArgumentParser(description="Run evaluation")
    parser.add_argument("--dataset", required=True, help="Dataset path")
    parser.add_argument("--output", help="Output report path")

    args = parser.parse_args()

    runner = EvaluationRunner(model_fn=dummy_model)
    results = runner.evaluate(args.dataset)

    report = generate_report(results)
    print(report)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)


if __name__ == "__main__":
    main()
