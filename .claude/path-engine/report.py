#!/usr/bin/env python3
"""
Generate progress report and update tracker.

This script creates a human-readable progress report.
Uses only Python stdlib.
"""

import json
from datetime import datetime
from pathlib import Path


def get_repo_root():
    """Get the repository root directory."""
    import subprocess
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True
    )
    return Path(result.stdout.strip())


def load_evaluation():
    """Load the latest evaluation results."""
    repo_root = get_repo_root()
    eval_file = repo_root / ".claude" / "memory" / "latest_evaluation.json"

    if not eval_file.exists():
        return None

    with open(eval_file) as f:
        return json.load(f)


def load_learner_profile():
    """Load the learner profile."""
    repo_root = get_repo_root()
    profile_path = repo_root / ".claude" / "memory" / "learner_profile.json"
    with open(profile_path) as f:
        return json.load(f)


def load_progress_log():
    """Load recent progress log entries."""
    repo_root = get_repo_root()
    log_path = repo_root / ".claude" / "memory" / "progress_log.jsonl"

    entries = []
    if log_path.exists():
        with open(log_path) as f:
            for line in f:
                line = line.strip()
                if line:
                    entries.append(json.loads(line))

    return entries[-10:]  # Last 10 entries


def generate_report():
    """Generate the progress report."""
    repo_root = get_repo_root()
    profile = load_learner_profile()
    evaluation = load_evaluation()
    progress = load_progress_log()

    level = profile.get("level", "Beginner")
    current_state = profile.get("current_state", {})
    month = current_state.get("current_month", 1)
    week = current_state.get("current_week", 1)

    # Build report content
    report_lines = [
        "# Progress Report",
        "",
        f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "---",
        "",
        "## Current Status",
        "",
        f"- **Level**: {level}",
        f"- **Month**: {month} of 12",
        f"- **Week**: {week} of 4",
        f"- **Progress**: {((month - 1) * 4 + week) / 48 * 100:.1f}% through curriculum",
        "",
    ]

    if evaluation:
        report_lines.extend([
            "## Latest Evaluation",
            "",
            f"- **Overall Score**: {evaluation.get('overall', 'N/A')}%",
            f"- **Status**: {evaluation.get('status', 'N/A')}",
            "",
            "### Dimension Scores",
            "",
        ])

        scores = evaluation.get("scores", {})
        for dimension, score in scores.items():
            bar = "█" * (score // 10) + "░" * (10 - score // 10)
            report_lines.append(f"- {dimension.capitalize()}: {bar} {score}%")

        report_lines.append("")

    # Add recent activity
    report_lines.extend([
        "## Recent Activity",
        "",
    ])

    if progress:
        for entry in progress[-5:]:
            timestamp = entry.get("timestamp", "")[:10]
            event = entry.get("event", "unknown")
            report_lines.append(f"- [{timestamp}] {event}")
    else:
        report_lines.append("- No recent activity logged")

    report_lines.extend([
        "",
        "---",
        "",
        "## Next Steps",
        "",
        "1. Review this week's objectives",
        "2. Complete pending tasks",
        "3. Log reflections in journal",
        "4. Run `/evaluate` at week end",
        "",
    ])

    report_content = "\n".join(report_lines)

    # Write tracker file
    tracker_path = repo_root / "paths" / level / "tracker.md"
    tracker_path.parent.mkdir(parents=True, exist_ok=True)

    with open(tracker_path, "w") as f:
        f.write(report_content)

    # Print report
    print("=" * 50)
    print("PROGRESS REPORT")
    print("=" * 50)
    print(report_content)
    print("=" * 50)
    print(f"\nReport saved to: {tracker_path}")

    return report_content


if __name__ == "__main__":
    generate_report()
