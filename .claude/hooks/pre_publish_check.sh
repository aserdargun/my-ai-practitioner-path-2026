#!/bin/bash
# Pre-Publish Check Hook
# Runs before publishing/sharing work

set -e

echo "=== Pre-Publish Check ==="
echo "Date: $(date)"

ERRORS=0

# Check for uncommitted changes
echo ""
echo "Checking for uncommitted changes..."
if [[ -n $(git status --porcelain) ]]; then
    echo "WARNING: Uncommitted changes found"
    git status --short
    ((ERRORS++))
else
    echo "OK: All changes committed"
fi

# Check for TODO comments
echo ""
echo "Checking for TODO comments..."
TODO_COUNT=$(grep -r "TODO" --include="*.py" . 2>/dev/null | wc -l || echo 0)
if [[ $TODO_COUNT -gt 0 ]]; then
    echo "WARNING: Found $TODO_COUNT TODO comments"
    grep -r "TODO" --include="*.py" . 2>/dev/null | head -5
else
    echo "OK: No TODO comments found"
fi

# Check for debug prints
echo ""
echo "Checking for debug prints..."
DEBUG_COUNT=$(grep -r "print(" --include="*.py" . 2>/dev/null | grep -v "test_" | wc -l || echo 0)
if [[ $DEBUG_COUNT -gt 5 ]]; then
    echo "WARNING: Found $DEBUG_COUNT print statements (consider logging)"
else
    echo "OK: Minimal print statements"
fi

# Check README exists
echo ""
echo "Checking documentation..."
if [[ -f "README.md" ]]; then
    echo "OK: README.md exists"
else
    echo "ERROR: README.md not found"
    ((ERRORS++))
fi

# Run tests
if command -v pytest &> /dev/null; then
    echo ""
    echo "Running tests..."
    if pytest --tb=short -q; then
        echo "OK: All tests pass"
    else
        echo "ERROR: Some tests failed"
        ((ERRORS++))
    fi
fi

# Run linting
if command -v ruff &> /dev/null; then
    echo ""
    echo "Running linter..."
    if ruff check . --quiet; then
        echo "OK: No linting errors"
    else
        echo "WARNING: Linting issues found"
    fi
fi

# Summary
echo ""
echo "=== Pre-Publish Summary ==="
if [[ $ERRORS -eq 0 ]]; then
    echo "All checks passed! Ready to publish."
    exit 0
else
    echo "Found $ERRORS issue(s). Please fix before publishing."
    exit 1
fi
