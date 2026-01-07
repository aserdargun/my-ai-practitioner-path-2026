# Adaptation Rules

How the learning path can be modified based on your progress.

## Allowed Mutations

The system can only make these four types of changes:

1. **Level Change**
2. **Month Reorder**
3. **Remediation Week**
4. **Project Swap**

No other modifications are permitted.

---

## 1. Level Change

**What**: Move between Beginner, Intermediate, or Advanced

### Upgrade Triggers

- Overall score 90%+ for 4 consecutive weeks
- Learner explicitly requests
- Completing curriculum ahead of schedule

### Downgrade Triggers

- Overall score <50% for 2+ weeks
- Learner explicitly requests
- Consistent struggle with concepts

### Constraints

- Only at month boundaries
- Requires learner approval
- Preserves completed work

### Example

```json
{
  "type": "level_change",
  "action": "upgrade",
  "from": "Beginner",
  "to": "Intermediate",
  "rationale": "4 weeks of excellent progress (92% avg)",
  "effective": "month_03_start"
}
```

---

## 2. Month Reorder

**What**: Swap the order of upcoming months

### Triggers

- Low engagement with current topic
- Learner interest in different topic
- Prerequisites already met

### Constraints

- Only affects future months
- Stay within tier scope (Beginner can't swap to Tier 2 content)
- Preserve dependency chains
- Requires learner approval

### Example

```json
{
  "type": "month_reorder",
  "action": "swap",
  "months": [5, 7],
  "rationale": "Learner more interested in ML than advanced Python",
  "constraints_checked": ["no_dependency_violation", "same_tier"]
}
```

---

## 3. Remediation Week

**What**: Insert a review week within a month

### Triggers

- Completion score <60%
- Quality score <50%
- Learner feels lost
- Concept gaps identified

### Constraints

- Maximum 1 remediation week per month
- Focuses on specific gaps
- Doesn't add new content
- Extends month by 1 week

### Example

```json
{
  "type": "remediation_week",
  "action": "insert",
  "month": 3,
  "after_week": 2,
  "focus": ["list_comprehensions", "file_io"],
  "rationale": "Struggling with Python fundamentals"
}
```

---

## 4. Project Swap

**What**: Replace a month's project with an equivalent one

### Triggers

- Project mismatched with learner goals
- Quality scores consistently low
- Learner not engaged with topic
- Technical blockers

### Constraints

- Same skill level as original
- Same learning objectives covered
- From approved project list
- Requires learner approval

### Example

```json
{
  "type": "project_swap",
  "action": "replace",
  "month": 4,
  "original_project": "cli_tool",
  "new_project": "web_scraper",
  "rationale": "Web scraping aligns better with data science goals",
  "skills_preserved": ["python", "file_io", "error_handling"]
}
```

---

## Adaptation Process

### 1. Evaluation

```
/evaluate
```

Scores your progress across dimensions.

### 2. Analysis

```
/adapt-path
```

Analyzes scores and proposes changes.

### 3. Review

You review proposals with rationale.

### 4. Approval

You approve or reject changes.

### 5. Apply

Approved changes are logged and applied.

---

## Proposal Format

```json
{
  "timestamp": "2026-02-15T10:00:00Z",
  "based_on_evaluation": "2026-02-14T18:00:00Z",
  "proposals": [
    {
      "type": "remediation_week",
      "action": "insert",
      "confidence": 0.8,
      "rationale": "Low completion score (55%)"
    }
  ]
}
```

### Confidence Levels

- **0.8+**: Strong recommendation
- **0.6-0.79**: Moderate recommendation
- **0.4-0.59**: Suggestion to consider
- **<0.4**: Optional consideration

---

## What Cannot Be Changed

The system cannot:

- Skip required content
- Add content from higher tiers
- Remove evaluation requirements
- Change scoring weights
- Bypass learner approval

---

## Manual Overrides

You can always manually:

- Request level change
- Propose month reorder
- Ask for remediation week
- Suggest project swap

Just discuss with Claude and log the decision:

```
/add-best-practice
Decision: Swapped project X for Y because...
```

---

## Decision Logging

All adaptations are logged in:

```
.claude/memory/decisions.jsonl
```

Format:
```json
{
  "timestamp": "2026-02-15T10:00:00Z",
  "decision": "remediation_week_inserted",
  "month": 3,
  "rationale": "Learner needed more time on fundamentals"
}
```

This creates an audit trail of all path changes.
