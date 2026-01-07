#!/usr/bin/env python3
"""
Evaluate learner progress based on signals.

This script reads from memory files and git history to score progress.
Uses only Python stdlib.
"""

import json
import os
import subprocess
from datetime import datetime, timedelta
from pathlib import Path


def get_repo_root():
    """Get the repository root directory."""
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True
    )
    return Path(result.stdout.strip())


def load_learner_profile(repo_root):
    """Load the learner profile."""
    profile_path = repo_root / ".claude" / "memory" / "learner_profile.json"
    with open(profile_path) as f:
        return json.load(f)


def get_recent_commits(days=7):
    """Get commit count for the last N days."""
    since_date = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    result = subprocess.run(
        ["git", "log", "--oneline", f"--since={since_date}", "--no-merges"],
        capture_output=True,
        text=True
    )
    commits = result.stdout.strip().split("\n")
    return len([c for c in commits if c])


def check_test_coverage(repo_root):
    """Check if tests exist and pass."""
    test_dirs = [
        repo_root / "tests",
        repo_root / "test",
    ]

    for test_dir in test_dirs:
        if test_dir.exists():
            test_files = list(test_dir.glob("test_*.py"))
            return len(test_files) > 0

    return False


def check_documentation(repo_root):
    """Check documentation completeness."""
    readme = repo_root / "README.md"
    docs_dir = repo_root / "docs"

    score = 0
    if readme.exists():
        score += 50
    if docs_dir.exists():
        score += 50

    return score


def calculate_completion_score(profile, repo_root):
    """Calculate completion score based on deliverables."""
    current_month = profile.get("current_state", {}).get("current_month", 1)
    level = profile.get("level", "Beginner")

    month_dir = repo_root / "paths" / level / f"month-{current_month:02d}"

    if not month_dir.exists():
        return 50  # Default if month folder doesn't exist yet

    # Check for completed deliverables
    readme = month_dir / "README.md"
    if readme.exists():
        with open(readme) as f:
            content = f.read()
            checked = content.count("[x]") + content.count("[X]")
            unchecked = content.count("[ ]")
            total = checked + unchecked
            if total > 0:
                return int((checked / total) * 100)

    return 50


def calculate_quality_score(repo_root):
    """Calculate quality score based on tests and linting."""
    score = 50  # Base score

    # Check for tests
    if check_test_coverage(repo_root):
        score += 25

    # Check for pyproject.toml or setup.py
    if (repo_root / "pyproject.toml").exists():
        score += 15
    elif (repo_root / "setup.py").exists():
        score += 10

    # Check for type hints in Python files
    py_files = list(repo_root.glob("**/*.py"))[:10]  # Sample first 10
    type_hint_count = 0
    for py_file in py_files:
        try:
            with open(py_file) as f:
                content = f.read()
                if "->" in content or ": str" in content or ": int" in content:
                    type_hint_count += 1
        except Exception:
            pass

    if type_hint_count > 0:
        score += 10

    return min(score, 100)


def calculate_understanding_score(repo_root, profile):
    """Calculate understanding score based on reflections."""
    level = profile.get("level", "Beginner")
    journal_dir = repo_root / "paths" / level / "journal"

    if not journal_dir.exists():
        return 50

    # Check for journal entries
    entries = list(journal_dir.glob("*.md"))
    if len(entries) == 0:
        return 40
    elif len(entries) < 4:
        return 60
    else:
        return 80


def calculate_consistency_score():
    """Calculate consistency score based on commit patterns."""
    commits = get_recent_commits(days=7)

    if commits == 0:
        return 20
    elif commits < 3:
        return 50
    elif commits < 7:
        return 75
    else:
        return 90


def run_evaluation():
    """Run the full evaluation."""
    repo_root = get_repo_root()
    profile = load_learner_profile(repo_root)

    scores = {
        "completion": calculate_completion_score(profile, repo_root),
        "quality": calculate_quality_score(repo_root),
        "understanding": calculate_understanding_score(repo_root, profile),
        "consistency": calculate_consistency_score()
    }

    # Weighted average
    weights = {
        "completion": 0.30,
        "quality": 0.25,
        "understanding": 0.25,
        "consistency": 0.20
    }

    overall = sum(scores[k] * weights[k] for k in scores)

    # Determine status
    if overall >= 90:
        status = "Excelling"
    elif overall >= 70:
        status = "On Track"
    elif overall >= 50:
        status = "Needs Support"
    else:
        status = "At Risk"

    result = {
        "timestamp": datetime.now().isoformat(),
        "level": profile.get("level", "Beginner"),
        "month": profile.get("current_state", {}).get("current_month", 1),
        "week": profile.get("current_state", {}).get("current_week", 1),
        "scores": scores,
        "overall": round(overall, 1),
        "status": status
    }

    # Print results
    print("=" * 50)
    print("EVALUATION RESULTS")
    print("=" * 50)
    print(f"Level: {result['level']}")
    print(f"Month: {result['month']}, Week: {result['week']}")
    print()
    print("Scores:")
    for dimension, score in scores.items():
        print(f"  {dimension.capitalize()}: {score}%")
    print()
    print(f"Overall: {result['overall']}% ({result['status']})")
    print("=" * 50)

    # Save to file
    eval_file = repo_root / ".claude" / "memory" / "latest_evaluation.json"
    with open(eval_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\nResults saved to: {eval_file}")

    return result


if __name__ == "__main__":
    run_evaluation()
