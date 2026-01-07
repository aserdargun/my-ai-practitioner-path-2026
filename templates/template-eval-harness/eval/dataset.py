"""Test dataset handling."""

import json
from pathlib import Path
from typing import List
from dataclasses import dataclass


@dataclass
class TestCase:
    """A single test case."""
    id: str
    input: str
    expected: str
    category: str = "default"
    metadata: dict = None


def load_dataset(filepath: str) -> List[TestCase]:
    """Load test cases from JSON file."""
    with open(filepath, "r") as f:
        data = json.load(f)

    test_cases = []
    for item in data:
        test_cases.append(TestCase(
            id=item.get("id", f"test_{len(test_cases)}"),
            input=item["input"],
            expected=item["expected"],
            category=item.get("category", "default"),
            metadata=item.get("metadata")
        ))

    return test_cases


def save_dataset(test_cases: List[TestCase], filepath: str) -> None:
    """Save test cases to JSON file."""
    data = []
    for tc in test_cases:
        data.append({
            "id": tc.id,
            "input": tc.input,
            "expected": tc.expected,
            "category": tc.category,
            "metadata": tc.metadata
        })

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)


def create_sample_dataset(filepath: str) -> None:
    """Create a sample evaluation dataset."""
    sample = [
        {
            "id": "test_001",
            "input": "Hello world",
            "expected": "positive",
            "category": "greeting"
        },
        {
            "id": "test_002",
            "input": "This is bad",
            "expected": "negative",
            "category": "sentiment"
        },
        {
            "id": "test_003",
            "input": "The weather is nice today",
            "expected": "positive",
            "category": "weather"
        }
    ]

    with open(filepath, "w") as f:
        json.dump(sample, f, indent=2)
