# Evaluation Rubric

How your progress is scored in the learning system.

## Scoring Overview

Your progress is evaluated across four dimensions:

| Dimension | Weight | What It Measures |
|-----------|--------|------------------|
| Completion | 30% | Tasks and deliverables finished |
| Quality | 25% | Code quality, tests, documentation |
| Understanding | 25% | Reflections and explanations |
| Consistency | 20% | Regular engagement and commits |

---

## Completion (30%)

Measures what you've finished.

### Signals

- Checked items in week/month READMEs
- Completed project deliverables
- Submitted reflections

### Scoring

| Score | Criteria |
|-------|----------|
| 90-100% | All required tasks complete, stretch goals attempted |
| 70-89% | All required tasks complete |
| 50-69% | Most required tasks complete (>75%) |
| 30-49% | Some required tasks complete (50-75%) |
| 0-29% | Few tasks complete (<50%) |

### How to Improve

- Check off tasks as you complete them
- Submit all required deliverables
- Don't skip reflection entries

---

## Quality (25%)

Measures how well you build.

### Signals

- Test coverage
- Code organization
- Documentation completeness
- Error handling
- Following best practices

### Scoring

| Score | Criteria |
|-------|----------|
| 90-100% | Tests >80%, docs complete, clean code, good error handling |
| 70-89% | Tests >60%, docs exist, mostly clean code |
| 50-69% | Some tests, basic docs, code works |
| 30-49% | Few tests, minimal docs |
| 0-29% | No tests, no docs |

### How to Improve

- Write tests for your code
- Add docstrings and comments
- Handle errors gracefully
- Use `/harden` command

---

## Understanding (25%)

Measures how deeply you grasp concepts.

### Signals

- Journal reflections
- Explanation quality
- Concept connections
- Problem-solving approach

### Scoring

| Score | Criteria |
|-------|----------|
| 90-100% | Deep reflections, connects concepts, teaches others |
| 70-89% | Good reflections, understands why |
| 50-69% | Basic reflections, follows patterns |
| 30-49% | Minimal reflections |
| 0-29% | No reflections |

### How to Improve

- Write weekly journal entries
- Explain what you learned in your own words
- Connect new concepts to previous ones
- Use `/retro` command

---

## Consistency (20%)

Measures regular engagement.

### Signals

- Commit frequency
- Session regularity
- Progress pattern
- Week-over-week activity

### Scoring

| Score | Criteria |
|-------|----------|
| 90-100% | Daily commits, consistent weekly pattern |
| 70-89% | Regular commits (4+ per week), steady progress |
| 50-69% | Some commits (2-3 per week) |
| 30-49% | Sporadic commits (1 per week) |
| 0-29% | Long gaps, minimal activity |

### How to Improve

- Commit small changes frequently
- Set a regular learning schedule
- Even 15 minutes counts
- Use `/status` daily

---

## Overall Status

Your overall score determines your status:

| Score | Status | Meaning |
|-------|--------|---------|
| 90%+ | Excelling | Consider acceleration |
| 70-89% | On Track | Continue current path |
| 50-69% | Needs Support | Consider remediation |
| <50% | At Risk | Path adaptation recommended |

---

## Triggering Adaptations

Low scores can trigger adaptation proposals:

### Remediation Week

Triggered when:
- Completion < 60% for 2+ weeks
- Understanding < 50%
- Quality < 50%

### Project Swap

Triggered when:
- Quality consistently low
- Project seems mismatched

### Level Change

Triggered when:
- Excelling for 4+ weeks (upgrade)
- At Risk for 2+ weeks (adjustment)

---

## Running Evaluations

### Command

```
/evaluate
```

### Manual

```bash
python .claude/path-engine/evaluate.py
```

### Output

```
EVALUATION RESULTS
==================
Level: Beginner
Month: 2, Week: 3

Scores:
  Completion: 85%
  Quality: 70%
  Understanding: 90%
  Consistency: 80%

Overall: 81% (On Track)
```

---

## Self-Evaluation Tips

Before running `/evaluate`, ask yourself:

1. **Completion**: Did I finish what I planned?
2. **Quality**: Does my code have tests? Is it documented?
3. **Understanding**: Can I explain what I learned?
4. **Consistency**: Did I work on this regularly?

Use these questions to self-correct before the system evaluates you.
