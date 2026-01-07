# /plan-week Command

Generate a learning plan for the current week.

## Usage

```
/plan-week
```

## Behavior

1. Check current month and week from profile
2. Read month curriculum for objectives
3. Consider learner's available hours
4. Generate balanced weekly plan
5. Write plan to journal

## Output Format

```markdown
## Week Plan: Week [X] of Month [XX]

### Objectives
- [ ] Primary objective 1
- [ ] Primary objective 2

### Tasks
| Task | Est. Hours | Priority |
|------|------------|----------|
| Task 1 description | 2h | High |
| Task 2 description | 3h | High |
| Task 3 description | 2h | Medium |

### Reflection Prompt
[Question to consider this week]

### Stretch Goals (Optional)
- [ ] Advanced task if time permits
```

## Considerations

- Respect learner's weekly hour budget
- Balance theory and practice
- Include reflection time
- Leave buffer for unexpected challenges
