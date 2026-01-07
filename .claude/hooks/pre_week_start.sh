#!/bin/bash
# Pre-Week Start Hook
# Runs at the beginning of each learning week

set -e

echo "=== Pre-Week Start Hook ==="
echo "Date: $(date)"

# Check git status
echo ""
echo "Git Status:"
git status --short

# Check for uncommitted changes
if [[ -n $(git status --porcelain) ]]; then
    echo ""
    echo "WARNING: You have uncommitted changes from last week."
    echo "Consider committing or stashing before starting new week."
fi

# Check Python environment
echo ""
echo "Python Environment:"
python --version 2>/dev/null || echo "Python not found in PATH"

# Run linting if ruff is installed
if command -v ruff &> /dev/null; then
    echo ""
    echo "Running ruff check..."
    ruff check . --statistics || true
fi

# Run tests if pytest is installed
if command -v pytest &> /dev/null; then
    echo ""
    echo "Running tests..."
    pytest --tb=no -q || true
fi

echo ""
echo "=== Ready to start your week! ==="
