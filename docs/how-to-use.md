# How to Use This Learning System

A complete guide to using the AI Practitioner Booster 2026.

## Getting Started

### Prerequisites

- Python 3.11+ installed
- Git installed
- VS Code (recommended)
- Claude Code access

### First Steps

1. **Clone your fork** (if you haven't already):
   ```bash
   git clone https://github.com/YOUR-USERNAME/my-ai-practitioner-path-2026.git
   cd my-ai-practitioner-path-2026
   ```

2. **Open in VS Code**:
   ```bash
   code .
   ```

3. **Connect Claude Code** to your repository

4. **Check your status**:
   ```
   /status
   ```

## Daily Workflow

### Morning Routine

1. Open Claude Code
2. Run `/status` to see where you left off
3. Review today's planned tasks
4. Start working on the highest priority item

### During Work

- Commit frequently with meaningful messages
- Use Claude Code to help with coding problems
- Take notes in your journal folder

### End of Day

- Commit any work in progress
- Note blockers or questions for tomorrow
- Quick reflection on what you learned

## Weekly Workflow

| Day | Activity |
|-----|----------|
| **Monday** | `/plan-week` - Set up weekly goals |
| **Tuesday-Thursday** | Build, learn, commit |
| **Friday** | `/evaluate` + `/retro` - Review and reflect |
| **Weekend** | Optional: stretch goals, publishing |

### Monday: Plan Your Week

```
/plan-week
```

This generates a weekly plan with:
- Objectives for the week
- Specific tasks with time estimates
- Reflection prompts

### Friday: Evaluate and Reflect

```
/evaluate
/retro
```

This helps you:
- Score your progress
- Identify what went well
- Note areas for improvement
- Plan adjustments

## Monthly Workflow

Each month has:
- A theme and objectives
- Weekly breakdowns
- A main project
- Reflection requirements

### Month Structure

```
paths/Beginner/month-XX/
├── README.md        # Month overview and objectives
├── week-1.md        # Week 1 plan
├── week-2.md        # Week 2 plan
├── week-3.md        # Week 3 plan
├── week-4.md        # Week 4 plan
└── project/         # Month's main project
```

### End of Month

1. Complete the month's project
2. Write a month-end reflection
3. Run `/evaluate` for final assessment
4. Check if adaptations are suggested with `/adapt-path`

## Using Commands

### Essential Commands

| Command | When to Use |
|---------|-------------|
| `/status` | Start of each session |
| `/plan-week` | Start of each week |
| `/evaluate` | End of each week |
| `/debug-learning` | When stuck |

### All Commands

See [commands.md](commands.md) for the complete list.

## Working with Claude

### Asking for Help

- Be specific about what you're trying to do
- Share relevant code or error messages
- Mention what you've already tried

### Good Examples

```
I'm working on the CSV parser project from Month 02.
I'm getting a KeyError when processing this file.
Here's my code: [paste code]
Here's the error: [paste error]
```

### Learning Together

Claude can:
- Explain concepts
- Review your code
- Suggest improvements
- Help debug issues
- Guide project implementation

## Tracking Progress

### Memory System

Your progress is tracked in:
- `.claude/memory/progress_log.jsonl` - Event history
- `.claude/memory/decisions.jsonl` - Important decisions
- `.claude/memory/best_practices.md` - Your learnings

### Journal

Keep reflections in:
- `paths/Beginner/journal/` - Your journal entries

### Evaluation

Run the evaluation engine:
```bash
python .claude/path-engine/evaluate.py
```

## Getting Unstuck

### If You're Struggling

1. Run `/debug-learning`
2. Take a break and return fresh
3. Break the problem into smaller pieces
4. Check if you need a remediation week

### If You're Bored

1. Try stretch goals
2. Consider upgrading to Intermediate level
3. Build something extra with what you've learned

## Best Practices

1. **Commit often** - Small, frequent commits are better
2. **Write tests** - They catch bugs early
3. **Document as you go** - Don't wait until the end
4. **Reflect regularly** - Learning compounds
5. **Ship MVPs** - Done is better than perfect

## Next Steps

1. Go to your [Dashboard](../paths/Beginner/README.md)
2. Run `/status` to see your current state
3. Start with Month 01's curriculum
