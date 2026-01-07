# Commands Guide

Complete reference for all available commands in the learning system.

## Quick Reference

| Command | Purpose | Agent |
|---------|---------|-------|
| `/status` | Show current progress | Evaluator |
| `/plan-week` | Create weekly plan | Planner |
| `/start-week` | Initialize week | Planner |
| `/ship-mvp` | Ship minimum viable | Builder |
| `/harden` | Add tests, docs | Reviewer |
| `/publish` | Prepare for demo | Coach |
| `/retro` | Run retrospective | Coach |
| `/evaluate` | Run evaluation | Evaluator |
| `/adapt-path` | Propose changes | Evaluator |
| `/add-best-practice` | Save a learning | Coach |
| `/debug-learning` | Help when stuck | Coach |
| `/report` | Generate report | Evaluator |

---

## Planning Commands

### /status

Show your current learning status.

**When to use**: At the start of each session

**Output includes**:
- Current level, month, and week
- Task completion status
- Identified blockers
- Suggested next steps

**Example**:
```
/status

## Current Status
Level: Beginner
Month: 02 - Python Fundamentals
Week: 3 of 4

This Week's Progress:
- [x] List comprehensions
- [x] File I/O practice
- [ ] CSV parser (in progress)

Next Steps:
1. Complete CSV parser
2. Add unit tests
```

### /plan-week

Generate a learning plan for the current week.

**When to use**: Monday, start of each week

**Output includes**:
- Weekly objectives
- Specific tasks with estimates
- Reflection prompts
- Stretch goals

### /start-week

Initialize the week with setup and hooks.

**When to use**: After `/plan-week` on Monday

**Actions**:
- Runs pre_week_start.sh hook
- Creates journal entry for the week
- Sets up any required files

---

## Building Commands

### /ship-mvp

Ship a minimum viable version of your current project.

**When to use**: When you have a working feature

**Output includes**:
- MVP checklist
- Core features status
- Testing requirements
- Documentation needs

**Example**:
```
/ship-mvp

## MVP Checklist

Core Features:
- [x] POST /predict endpoint
- [x] Basic model loading
- [ ] Input validation

Testing:
- [ ] Unit tests for core logic
- [ ] Integration test for API

Documentation:
- [ ] README with usage
- [ ] Example requests
```

### /harden

Add tests, documentation, and error handling.

**When to use**: After MVP is working

**Output includes**:
- Current test coverage
- Error handling gaps
- Documentation checklist
- Security considerations

---

## Review Commands

### /retro

Run a retrospective on your recent work.

**When to use**: Friday, end of each week

**Prompts for**:
- What went well?
- What was challenging?
- What will you do differently?
- Key learnings

### /evaluate

Run a comprehensive progress evaluation.

**When to use**: End of each week

**Runs**: `path-engine/evaluate.py`

**Scores**:
- Completion (30%)
- Quality (25%)
- Understanding (25%)
- Consistency (20%)

### /adapt-path

Propose curriculum adaptations based on evaluation.

**When to use**: When evaluation suggests changes

**Runs**: `path-engine/adapt.py`

**Can propose**:
- Level change
- Month reorder
- Remediation week
- Project swap

### /report

Generate a progress report.

**When to use**: Anytime, for status overview

**Runs**: `path-engine/report.py`

**Creates**: `paths/Beginner/tracker.md`

---

## Support Commands

### /debug-learning

Get help when stuck on learning.

**When to use**: When confused or blocked

**Claude will**:
- Ask clarifying questions
- Break down the problem
- Identify knowledge gaps
- Suggest resources
- Provide incremental steps

### /add-best-practice

Save a learning to your best practices document.

**When to use**: When you learn something worth remembering

**Example**:
```
/add-best-practice

What's the learning? Always write tests before refactoring.

Added to best_practices.md:
## Testing
- **Always write tests before refactoring** - Tests give
  confidence that refactoring doesn't break functionality.
```

### /publish

Prepare your work for demo or write-up.

**When to use**: When ready to share

**Runs**: pre_publish_check.sh hook

**Checks**:
- All changes committed
- Tests passing
- Documentation complete
- No debug code

---

## Command Flow Examples

### Typical Week

```
Monday:    /plan-week -> /start-week
Tuesday:   /status -> [work] -> commit
Wednesday: /status -> [work] -> commit
Thursday:  /status -> [work] -> /ship-mvp -> commit
Friday:    /evaluate -> /retro -> commit
```

### When Stuck

```
/debug-learning
[Claude helps identify the issue]
[Work on the specific problem]
/status
[Continue with plan]
```

### End of Month

```
/evaluate
/adapt-path  (if needed)
/publish     (if sharing)
/report
```
