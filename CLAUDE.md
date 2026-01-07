# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Overview

This is an AI-driven learning system for becoming an AI practitioner in 2026. The current learner level is **Beginner**, which means the curriculum focuses on Tier 1 skills only.

## Key Directories

- `.claude/` - All Claude capabilities (agents, commands, skills, hooks, memory, mcp, path-engine)
- `docs/` - Documentation for learners
- `paths/Beginner/` - The learner's main dashboard and 12-month curriculum
- `templates/` - Starter templates for projects
- `stacks/` - Technology tier definitions

## Commands

When the learner uses commands, route them to the appropriate agent:

| Command | Primary Agent | Description |
|---------|--------------|-------------|
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

See `.claude/commands/catalog.md` for full details.

## Memory System

The memory system lives in `.claude/memory/`:
- `learner_profile.json` - Goals, constraints, schedule
- `progress_log.jsonl` - Timestamped events (append-only)
- `decisions.jsonl` - Important decisions (append-only)
- `best_practices.md` - Living document of learnings

## Evaluation Loop

1. Run `.claude/path-engine/evaluate.py` to score progress
2. Run `.claude/path-engine/adapt.py` to propose changes
3. Run `.claude/path-engine/report.py` to update tracker

## Beginner Tier Focus

For Beginner level, focus on Tier 1 technologies:
- **Languages**: Python, SQL, R, Bash
- **Frameworks**: Flask, Django
- **Libraries**: Pandas, NumPy, Matplotlib, seaborn, NLTK
- **Tools**: VS Code, Jupyter, Git/GitHub, Streamlit
- **Skills**: Data Science, ETL, Predictive Analytics, Time Series, Deep Learning (intro)

Do not introduce Tier 2 or Tier 3 technologies unless the learner explicitly requests an upgrade.

## Code Style

- Python: Follow PEP 8, use type hints
- Use `ruff` for linting
- Use `pytest` for testing
- Keep dependencies minimal and pinned
