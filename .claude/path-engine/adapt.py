#!/usr/bin/env python3
"""
Propose path adaptations based on evaluation results.

This script reads evaluation results and proposes allowed mutations.
Uses only Python stdlib.
"""

import json
from datetime import datetime
from pathlib import Path


# Allowed adaptation types
ALLOWED_MUTATIONS = [
    "level_change",      # Beginner <-> Intermediate <-> Advanced
    "month_reorder",     # Swap upcoming months within tier
    "remediation_week",  # Insert review week
    "project_swap"       # Replace with equivalent project
]


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


def analyze_for_adaptations(evaluation, profile):
    """Analyze evaluation and propose adaptations."""
    proposals = []
    overall = evaluation.get("overall", 50)
    scores = evaluation.get("scores", {})
    current_level = profile.get("level", "Beginner")

    # Check for level change opportunity
    if overall >= 90 and current_level == "Beginner":
        proposals.append({
            "type": "level_change",
            "action": "upgrade",
            "from": "Beginner",
            "to": "Intermediate",
            "rationale": "Excellent progress. Consider advancing to Intermediate level.",
            "confidence": 0.7
        })
    elif overall < 50:
        proposals.append({
            "type": "remediation_week",
            "action": "insert",
            "rationale": "Progress is below target. Consider a remediation week to reinforce concepts.",
            "confidence": 0.8
        })

    # Check for specific dimension issues
    if scores.get("completion", 100) < 60:
        proposals.append({
            "type": "remediation_week",
            "action": "insert",
            "focus": "completion",
            "rationale": "Low completion rate. Consider extending current month or adding review time.",
            "confidence": 0.75
        })

    if scores.get("quality", 100) < 60:
        proposals.append({
            "type": "project_swap",
            "action": "suggest",
            "rationale": "Quality scores indicate need for simpler project. Consider swapping to a more focused project.",
            "confidence": 0.6
        })

    if scores.get("consistency", 100) < 40:
        proposals.append({
            "type": "month_reorder",
            "action": "suggest",
            "rationale": "Low engagement detected. Consider reordering to bring more interesting topics forward.",
            "confidence": 0.5
        })

    return proposals


def format_proposal(proposal):
    """Format a proposal for display."""
    lines = [
        f"Type: {proposal['type']}",
        f"Action: {proposal['action']}",
        f"Rationale: {proposal['rationale']}",
        f"Confidence: {proposal['confidence']*100:.0f}%"
    ]
    if "from" in proposal:
        lines.insert(1, f"Change: {proposal['from']} -> {proposal['to']}")
    if "focus" in proposal:
        lines.insert(1, f"Focus: {proposal['focus']}")
    return "\n  ".join(lines)


def run_adaptation():
    """Run the adaptation analysis."""
    evaluation = load_evaluation()
    profile = load_learner_profile()

    if not evaluation:
        print("No evaluation found. Run evaluate.py first.")
        return None

    proposals = analyze_for_adaptations(evaluation, profile)

    print("=" * 50)
    print("ADAPTATION PROPOSALS")
    print("=" * 50)
    print(f"Based on evaluation from: {evaluation.get('timestamp', 'unknown')}")
    print(f"Current Status: {evaluation.get('status', 'unknown')}")
    print()

    if not proposals:
        print("No adaptations recommended at this time.")
        print("Continue on current path.")
    else:
        print(f"Found {len(proposals)} potential adaptation(s):\n")
        for i, proposal in enumerate(proposals, 1):
            print(f"Proposal {i}:")
            print(f"  {format_proposal(proposal)}")
            print()

    print("=" * 50)
    print("\nAllowed mutation types:")
    for mutation in ALLOWED_MUTATIONS:
        print(f"  - {mutation}")
    print()
    print("Note: All adaptations require learner approval before applying.")

    # Save proposals
    repo_root = get_repo_root()
    proposals_file = repo_root / ".claude" / "memory" / "latest_proposals.json"

    result = {
        "timestamp": datetime.now().isoformat(),
        "based_on_evaluation": evaluation.get("timestamp"),
        "proposals": proposals
    }

    with open(proposals_file, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\nProposals saved to: {proposals_file}")

    return proposals


if __name__ == "__main__":
    run_adaptation()
