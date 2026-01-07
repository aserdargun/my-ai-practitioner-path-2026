# Agents Guide

Understanding the six specialized agents that power your learning system.

## Overview

The learning system uses six specialized agents, each with a specific role:

```
┌─────────────────────────────────────────────────────────────┐
│                    LEARNING SYSTEM                          │
├─────────────┬─────────────┬─────────────┬─────────────────┤
│   PLANNER   │   BUILDER   │  REVIEWER   │   EVALUATOR     │
│  Plan work  │ Build code  │ Check qual  │  Score prog     │
├─────────────┴─────────────┴─────────────┴─────────────────┤
│              COACH                  RESEARCHER             │
│          Mentor & guide           Find resources           │
└─────────────────────────────────────────────────────────────┘
```

---

## Planner Agent

**Role**: Weekly and monthly planning

**Commands**: `/plan-week`, `/start-week`

**Responsibilities**:
- Create weekly learning plans
- Break down monthly goals
- Balance learning with available time
- Coordinate with other agents

**When Planner Helps**:
- Start of each week
- When prioritizing tasks
- When feeling overwhelmed
- When adjusting schedule

**Example Interaction**:
```
User: /plan-week

Planner: Based on your Month 02 focus and 10 hours available:

## Week 3 Plan

### Objectives
- Master list comprehensions
- Practice file I/O

### Tasks
- Complete exercises (2h)
- Build CSV parser (3h)
- Write tests (2h)
- Reflect (1h)
```

---

## Builder Agent

**Role**: Implementation guidance

**Commands**: `/ship-mvp`

**Responsibilities**:
- Guide through implementations
- Help debug code issues
- Provide code reviews
- Assist in shipping MVPs

**When Builder Helps**:
- Writing new code
- Debugging issues
- Getting something working
- Shipping a version

**Example Interaction**:
```
User: /ship-mvp

Builder: Let's ship your API. Here's the plan:

## MVP Checklist
- [x] Basic endpoint works
- [ ] Add input validation
- [ ] Write one test
- [ ] Update README
```

---

## Reviewer Agent

**Role**: Code quality and hardening

**Commands**: `/harden`

**Responsibilities**:
- Review code quality
- Suggest improvements
- Ensure test coverage
- Check documentation

**When Reviewer Helps**:
- After MVP is working
- Before sharing code
- When improving quality
- Before merging code

**Example Interaction**:
```
User: /harden

Reviewer: Here's your hardening report:

## Test Coverage: 40%
Missing tests for:
- Error handling
- Edge cases

## Documentation
- README exists ✓
- API docs missing
```

---

## Evaluator Agent

**Role**: Progress assessment

**Commands**: `/status`, `/evaluate`, `/adapt-path`, `/report`

**Responsibilities**:
- Assess progress
- Score deliverables
- Propose adaptations
- Generate reports

**When Evaluator Helps**:
- Checking current status
- End of week reviews
- When needing path changes
- Generating progress reports

**Example Interaction**:
```
User: /evaluate

Evaluator: Week 3 Evaluation:

## Scores
- Completion: 85%
- Quality: 70%
- Understanding: 90%
- Consistency: 80%

## Overall: 81% (On Track)
```

---

## Coach Agent

**Role**: Mentoring and support

**Commands**: `/retro`, `/debug-learning`, `/publish`, `/add-best-practice`

**Responsibilities**:
- Facilitate retrospectives
- Help with learning blocks
- Guide publishing
- Maintain best practices

**When Coach Helps**:
- Weekly reflections
- When feeling stuck
- Before publishing work
- Capturing learnings

**Example Interaction**:
```
User: /debug-learning

Coach: What are you stuck on?

User: I don't understand decorators.

Coach: Let's break it down:
1. A decorator wraps a function
2. Here's a simple example...
3. Try this exercise...
```

---

## Researcher Agent

**Role**: Learning resources

**Commands**: (Supports other agents)

**Responsibilities**:
- Find learning resources
- Explain concepts
- Compare approaches
- Provide context

**When Researcher Helps**:
- Learning new concepts
- Comparing technologies
- Finding documentation
- Understanding context

**Example Interaction**:
```
User: Explain what a DataFrame is.

Researcher: A DataFrame is Pandas' main data structure:
- 2-dimensional (rows/columns)
- Like a spreadsheet or SQL table
- Each column can have different types

Here's a quick example...
```

---

## Agent Collaboration

Agents work together seamlessly:

1. **Planner → Builder**: Plan leads to implementation
2. **Builder → Reviewer**: Build leads to quality check
3. **Reviewer → Evaluator**: Quality feeds into scoring
4. **Evaluator → Coach**: Scores inform coaching
5. **Coach → Planner**: Learnings inform next plan
6. **Researcher → All**: Resources support everyone

---

## Accessing Agents

You don't need to call agents directly. Use commands and the system routes to the right agent:

| If you want to... | Use command | Agent handles it |
|-------------------|-------------|------------------|
| Plan your week | `/plan-week` | Planner |
| Ship code | `/ship-mvp` | Builder |
| Improve code | `/harden` | Reviewer |
| Check progress | `/evaluate` | Evaluator |
| Get unstuck | `/debug-learning` | Coach |
| Learn concept | Ask Claude | Researcher |

---

## Technical Details

Agent definitions are in: `.claude/agents/`

Each agent file contains:
- Role description
- Responsibilities
- Primary commands
- Behavior specifications
- Integration points
- Example interactions
