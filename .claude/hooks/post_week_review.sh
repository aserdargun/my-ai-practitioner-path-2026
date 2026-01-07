#!/bin/bash
# Post-Week Review Hook
# Runs at the end of each learning week

set -e

echo "=== Post-Week Review Hook ==="
echo "Date: $(date)"

# Git summary for the week
echo ""
echo "This Week's Commits:"
git log --oneline --since="7 days ago" --no-merges | head -20

# Count commits
COMMIT_COUNT=$(git log --oneline --since="7 days ago" --no-merges | wc -l)
echo ""
echo "Total commits this week: $COMMIT_COUNT"

# Files changed
echo ""
echo "Files Changed This Week:"
git diff --stat HEAD~$COMMIT_COUNT 2>/dev/null | tail -5 || echo "Unable to compute diff"

# Lines of code added/removed
echo ""
echo "Lines Changed:"
git diff --shortstat HEAD~$COMMIT_COUNT 2>/dev/null || echo "Unable to compute stats"

# Check test status
if command -v pytest &> /dev/null; then
    echo ""
    echo "Test Results:"
    pytest --tb=no -q 2>/dev/null || echo "Some tests may have failed"
fi

echo ""
echo "=== Week Review Complete ==="
echo ""
echo "Next steps:"
echo "1. Run /retro to reflect on your week"
echo "2. Run /evaluate to score your progress"
echo "3. Update your journal with reflections"
