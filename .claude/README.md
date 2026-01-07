# .claude/ — Claude Capabilities

This folder contains all Claude Code configurations, agents, commands, skills, hooks, memory, MCP tools, and the path engine.

## Structure

```
.claude/
├── README.md           # This file
├── agents/             # AI agent definitions
├── commands/           # Command catalog and definitions
├── skills/             # Skill playbooks for common tasks
├── hooks/              # Automation scripts
├── memory/             # Learning profile and progress logs
├── mcp/                # Model Context Protocol tools
└── path-engine/        # Evaluation and adaptation scripts
```

## Agents

Six specialized agents work together:

| Agent | Role | Primary Commands |
|-------|------|------------------|
| [Planner](agents/planner.md) | Weekly/monthly planning | `/plan-week`, `/start-week` |
| [Builder](agents/builder.md) | Implementation guidance | `/ship-mvp` |
| [Reviewer](agents/reviewer.md) | Code quality, hardening | `/harden` |
| [Evaluator](agents/evaluator.md) | Progress assessment | `/evaluate`, `/adapt-path`, `/report` |
| [Coach](agents/coach.md) | Mentoring, retrospectives | `/retro`, `/debug-learning`, `/publish` |
| [Researcher](agents/researcher.md) | Learning resources | Research tasks |

## Commands

All commands are defined in [commands/catalog.md](commands/catalog.md).

Key commands:
- `/status` - Show current progress
- `/plan-week` - Create weekly plan
- `/evaluate` - Run evaluation
- `/adapt-path` - Propose path changes

## Skills

Skill playbooks provide step-by-step guidance for common tasks:

- [EDA to Insight](skills/eda-to-insight.md)
- [Ship API](skills/ship-api.md)
- [Build RAG](skills/build-rag.md)
- [Run Evals](skills/run-evals.md)

## Hooks

Automation scripts for workflow events:

- `pre_week_start.sh` - Runs at week start
- `post_week_review.sh` - Runs after weekly review
- `pre_publish_check.sh` - Runs before publishing

## Memory

The memory system tracks your learning:

- `learner_profile.json` - Your goals and constraints
- `progress_log.jsonl` - Event history (append-only)
- `decisions.jsonl` - Important decisions (append-only)
- `best_practices.md` - Learnings document

## Path Engine

Python scripts (stdlib only) that power the evaluation loop:

- `evaluate.py` - Score your progress
- `adapt.py` - Propose path changes
- `report.py` - Generate reports

## MCP Tools

Model Context Protocol tool definitions for extending Claude's capabilities.
