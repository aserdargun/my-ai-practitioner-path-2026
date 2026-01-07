# my-ai-practitioner-path-2026

**AI Practitioner Booster 2026 — AI-driven, project-based learning system**

A complete learning operating system that provides a structured, AI-driven path for becoming an AI practitioner. The system continuously evaluates your progress and adapts to your learning pace.

---

## Your Learning Dashboard

**Current Level: Beginner** (Tier 1 focus for 2026)

👉 **[Go to Your Dashboard](paths/Beginner/README.md)** — Your main hub for tracking progress, weekly plans, and month-by-month curriculum.

---

## Quickstart (5 Minutes)

```bash
# 1. Check your current status
# In Claude Code, type:
/status

# 2. Plan your week
/plan-week

# 3. Evaluate your progress
/evaluate

# 4. Generate a progress report
/report
```

---

## How the AI-Driven Loop Works

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  EVALUATE   │────▶│    ADAPT    │────▶│   EXECUTE   │
│             │     │             │     │             │
│ Analyze     │     │ Adjust      │     │ Learn &     │
│ progress,   │     │ path based  │     │ build       │
│ signals     │     │ on scores   │     │ projects    │
└─────────────┘     └─────────────┘     └─────────────┘
       ▲                                       │
       └───────────────────────────────────────┘
```

1. **Evaluate**: Claude analyzes your commits, reflections, and project completion
2. **Adapt**: Based on signals, Claude proposes path modifications
3. **Execute**: You work on projects with Claude's guidance, then cycle repeats

---

## Daily Workflow

1. Open Claude Code connected to this repo
2. Run `/status` to see where you are
3. Work on your current week's tasks
4. Commit your work with meaningful messages
5. Log reflections in your journal

## Weekly Workflow

| Day | Activity |
|-----|----------|
| **Monday** | Run `/plan-week`, review goals |
| **Tue-Thu** | Build, learn, commit |
| **Friday** | Run `/evaluate`, reflect |
| **Weekend** | Optional: stretch goals, publish |

---

## Key Commands

| Command | Purpose |
|---------|---------|
| `/status` | See current progress and blockers |
| `/plan-week` | Generate this week's learning plan |
| `/evaluate` | Run evaluation on your progress |
| `/debug-learning` | Get help when stuck |
| `/ship-mvp` | Ship a minimum viable version |

See [docs/commands.md](docs/commands.md) for the complete guide.

---

## Repository Structure

```
/
├── README.md                 # This file
├── CLAUDE.md                 # Claude Code instructions
├── PROMPT.md                 # Repository generator prompt
│
├── .claude/                  # Claude capabilities
│   ├── agents/               # Agent definitions
│   ├── commands/             # Command catalog
│   ├── skills/               # Skill playbooks
│   ├── hooks/                # Automation hooks
│   ├── memory/               # Learning memory
│   ├── mcp/                  # MCP tools
│   └── path-engine/          # Evaluation engine
│
├── docs/                     # Documentation
│   ├── evaluation/           # Rubrics and scoring
│   └── publishing/           # How to share your work
│
├── stacks/                   # Technology tier definitions
│
├── paths/
│   └── Beginner/             # Your learning path
│       ├── journal/          # Weekly/monthly reflections
│       └── month-01..12/     # Monthly curriculum
│
├── templates/                # Project templates
│
└── .github/                  # GitHub templates & CI
```

---

## Navigation

| Document | Purpose |
|----------|---------|
| [Dashboard](paths/Beginner/README.md) | Your main learning hub |
| [How to Use](docs/how-to-use.md) | Getting started guide |
| [Commands](docs/commands.md) | All available commands |
| [Agents](docs/agents.md) | AI agent capabilities |
| [Skills](docs/skills-playbook.md) | Common task playbooks |
| [Evaluation](docs/evaluation/rubric.md) | How you're scored |
| [Claude Capabilities](.claude/README.md) | Technical details |

---

## Running the Engine Locally

```bash
# Evaluate progress
python .claude/path-engine/evaluate.py

# Get adaptation suggestions
python .claude/path-engine/adapt.py

# Generate report
python .claude/path-engine/report.py
```

---

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) first.

## Code of Conduct

This project follows the Contributor Covenant. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
