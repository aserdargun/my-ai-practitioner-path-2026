# /evaluate Command

Run a comprehensive evaluation of learning progress.

## Usage

```
/evaluate
```

## Behavior

1. Run `python .claude/path-engine/evaluate.py`
2. Parse evaluation results
3. Present scores and analysis
4. Provide recommendations

## Scoring Dimensions

| Dimension | Weight | Signals |
|-----------|--------|---------|
| Completion | 30% | Deliverables finished, tasks checked off |
| Quality | 25% | Test coverage, code review, docs |
| Understanding | 25% | Journal reflections, explanations |
| Consistency | 20% | Commit frequency, engagement pattern |

## Output Format

```markdown
## Evaluation Results

### Scores
- Completion: [X]%
- Quality: [X]%
- Understanding: [X]%
- Consistency: [X]%

### Overall: [X]% ([Status])

### Strengths
- [Positive observation 1]
- [Positive observation 2]

### Areas for Improvement
- [Suggestion 1]
- [Suggestion 2]

### Recommendation
[Continue/Adapt/Remediate] - [Explanation]
```

## Status Levels

- **Excelling** (90%+): Consider acceleration
- **On Track** (70-89%): Continue current path
- **Needs Support** (50-69%): Consider remediation
- **At Risk** (<50%): Trigger adaptation review
