# Hooks Guide

Automation scripts that run at key workflow moments.

## Overview

Hooks are shell scripts that automate checks and setup at important moments:

```
.claude/hooks/
├── pre_week_start.sh      # Runs at week start
├── post_week_review.sh    # Runs after weekly review
└── pre_publish_check.sh   # Runs before publishing
```

## Available Hooks

### pre_week_start.sh

**Triggered by**: `/start-week` command

**What it does**:
- Checks git status
- Warns about uncommitted changes
- Verifies Python environment
- Runs linting check
- Runs tests

**Example output**:
```
=== Pre-Week Start Hook ===
Date: Mon Jan 6 09:00:00 UTC 2026

Git Status:
 M src/app.py

WARNING: You have uncommitted changes from last week.

Python Environment:
Python 3.11.0

Running ruff check...
All checks passed!

Running tests...
5 passed

=== Ready to start your week! ===
```

### post_week_review.sh

**Triggered by**: After `/evaluate` or `/retro`

**What it does**:
- Shows this week's commits
- Counts total commits
- Shows files changed
- Reports test status

**Example output**:
```
=== Post-Week Review Hook ===

This Week's Commits:
abc1234 Add user authentication
def5678 Fix login bug
ghi9012 Add tests

Total commits this week: 3

Files Changed This Week:
 src/auth.py  | 50 ++
 tests/test_auth.py | 30 ++

Lines Changed:
 2 files changed, 80 insertions(+)

Test Results:
8 passed

=== Week Review Complete ===
```

### pre_publish_check.sh

**Triggered by**: `/publish` command

**What it does**:
- Checks for uncommitted changes
- Scans for TODO comments
- Counts debug prints
- Verifies README exists
- Runs all tests
- Runs linting

**Example output**:
```
=== Pre-Publish Check ===

Checking for uncommitted changes...
OK: All changes committed

Checking for TODO comments...
WARNING: Found 2 TODO comments

Checking for debug prints...
OK: Minimal print statements

Checking documentation...
OK: README.md exists

Running tests...
OK: All tests pass

Running linter...
OK: No linting errors

=== Pre-Publish Summary ===
All checks passed! Ready to publish.
```

## Running Hooks

### Automatic (via commands)

Hooks run automatically when you use commands:
- `/start-week` → pre_week_start.sh
- `/evaluate` → post_week_review.sh
- `/publish` → pre_publish_check.sh

### Manual

Run hooks directly from terminal:

```bash
bash .claude/hooks/pre_week_start.sh
bash .claude/hooks/post_week_review.sh
bash .claude/hooks/pre_publish_check.sh
```

## Platform Notes

### Linux / macOS

Hooks work out of the box:

```bash
chmod +x .claude/hooks/*.sh
bash .claude/hooks/pre_week_start.sh
```

### Windows

**Option 1: WSL (Recommended)**

```bash
# In WSL terminal
bash .claude/hooks/pre_week_start.sh
```

**Option 2: Git Bash**

```bash
# In Git Bash
bash .claude/hooks/pre_week_start.sh
```

**Option 3: Manual Steps**

If you can't run bash scripts, do the steps manually:

**pre_week_start.sh equivalent**:
```cmd
git status
python --version
ruff check .
pytest
```

**post_week_review.sh equivalent**:
```cmd
git log --oneline --since="7 days ago"
pytest
```

**pre_publish_check.sh equivalent**:
```cmd
git status
findstr /s "TODO" *.py
pytest
ruff check .
```

## Customizing Hooks

### Adding Checks

Edit the hook scripts to add your own checks:

```bash
# Add to pre_publish_check.sh

# Check for security issues
echo ""
echo "Checking for hardcoded secrets..."
if grep -r "API_KEY\s*=" --include="*.py" .; then
    echo "WARNING: Possible hardcoded API key"
    ((ERRORS++))
else
    echo "OK: No hardcoded secrets found"
fi
```

### Creating New Hooks

Create a new hook for your workflow:

```bash
#!/bin/bash
# .claude/hooks/pre_commit_check.sh
# Custom pre-commit checks

set -e

echo "=== Pre-Commit Check ==="

# Your checks here
ruff check .
pytest --tb=no -q

echo "=== Ready to commit! ==="
```

Make it executable:
```bash
chmod +x .claude/hooks/pre_commit_check.sh
```

## Troubleshooting

### Permission Denied

```bash
chmod +x .claude/hooks/*.sh
```

### Command Not Found

Ensure tools are installed:
```bash
pip install ruff pytest
```

### Script Fails on Windows Line Endings

Convert to Unix line endings:
```bash
sed -i 's/\r$//' .claude/hooks/*.sh
```

Or use dos2unix:
```bash
dos2unix .claude/hooks/*.sh
```
