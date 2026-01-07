# /status Command

Show current learning status and progress.

## Usage

```
/status
```

## Behavior

1. Read learner profile from `.claude/memory/learner_profile.json`
2. Determine current month and week
3. Check task completion in current month folder
4. Identify any blockers from progress log
5. Generate status report

## Output Format

```markdown
## Current Status

**Level**: [Beginner/Intermediate/Advanced]
**Month**: [XX] - [Month Title]
**Week**: [X] of 4

### This Week's Progress
- [x] Completed task 1
- [x] Completed task 2
- [ ] In progress task 3
- [ ] Not started task 4

### Blockers
[List any identified blockers or "None identified"]

### Next Steps
1. [Immediate next action]
2. [Following action]
3. [Third action]
```

## Data Sources

- `.claude/memory/learner_profile.json` - Level and start date
- `paths/Beginner/month-XX/README.md` - Current curriculum
- `.claude/memory/progress_log.jsonl` - Recent events
- Git commit history - Activity signal
