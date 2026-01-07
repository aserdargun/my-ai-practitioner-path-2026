# Command Catalog

This is the authoritative source for all available commands in the learning system.

## Quick Reference

| Command | Agent | Purpose |
|---------|-------|---------|
| `/status` | Evaluator | Show current progress |
| `/plan-week` | Planner | Create weekly plan |
| `/start-week` | Planner | Initialize week with hooks |
| `/ship-mvp` | Builder | Ship minimum viable version |
| `/harden` | Reviewer | Add tests, docs, error handling |
| `/publish` | Coach | Prepare for demo/write-up |
| `/retro` | Coach | Run retrospective |
| `/evaluate` | Evaluator | Run full evaluation |
| `/adapt-path` | Evaluator | Propose path changes |
| `/add-best-practice` | Coach | Add to best practices |
| `/debug-learning` | Coach | Help when stuck |
| `/report` | Evaluator | Generate progress report |

---

## Command Details

### /status

**Agent**: Evaluator
**Purpose**: Show current progress and identify blockers

**Output**:
- Current level, month, week
- Task completion status
- Identified blockers
- Next steps

---

### /plan-week

**Agent**: Planner
**Purpose**: Generate this week's learning plan

**Output**:
- Weekly objectives
- Specific tasks with time estimates
- Reflection prompt
- Optional stretch goals

---

### /start-week

**Agent**: Planner
**Purpose**: Initialize the week and run setup hooks

**Actions**:
- Run `pre_week_start.sh` hook
- Create week's journal entry
- Set up any required files

---

### /ship-mvp

**Agent**: Builder
**Purpose**: Ship a minimum viable version of current project

**Output**:
- MVP checklist
- Core features status
- Testing requirements
- Documentation needs

---

### /harden

**Agent**: Reviewer
**Purpose**: Add tests, documentation, and error handling

**Output**:
- Hardening report
- Test coverage analysis
- Error handling gaps
- Documentation checklist

---

### /publish

**Agent**: Coach
**Purpose**: Prepare work for demo or write-up

**Actions**:
- Run `pre_publish_check.sh` hook
- Review project completeness
- Generate demo script outline
- Draft blog post structure

---

### /retro

**Agent**: Coach
**Purpose**: Run a retrospective on recent work

**Output**:
- Guided reflection prompts
- Space for what went well
- Space for challenges
- Action items for next week

---

### /evaluate

**Agent**: Evaluator
**Purpose**: Run full evaluation on progress

**Actions**:
- Run `path-engine/evaluate.py`
- Score against rubric
- Identify strengths and gaps
- Generate recommendations

---

### /adapt-path

**Agent**: Evaluator
**Purpose**: Propose path changes based on evaluation

**Actions**:
- Run `path-engine/adapt.py`
- Analyze evaluation results
- Propose allowed mutations
- Explain rationale

---

### /add-best-practice

**Agent**: Coach
**Purpose**: Add a learning to the best practices document

**Actions**:
- Capture the learning
- Format appropriately
- Append to `memory/best_practices.md`

---

### /debug-learning

**Agent**: Coach
**Purpose**: Help when stuck on learning

**Output**:
- Problem breakdown
- Knowledge gap identification
- Resource suggestions
- Incremental next steps

---

### /report

**Agent**: Evaluator
**Purpose**: Generate progress report

**Actions**:
- Run `path-engine/report.py`
- Update tracker document
- Summarize progress
- Highlight achievements
