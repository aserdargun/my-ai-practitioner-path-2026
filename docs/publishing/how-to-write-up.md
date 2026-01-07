# How to Write Up Your Projects

A guide to documenting and writing about your learning projects.

## Why Write?

- Deepens your understanding
- Creates portfolio content
- Helps others learn
- Improves communication
- Builds your reputation

---

## Write-Up Types

### 1. Technical README

**Purpose**: Help others use your code

```markdown
# Project Name

Brief description.

## Installation

pip install -r requirements.txt

## Usage

python main.py --input data.csv

## API Reference

### endpoint_name
Description and parameters.

## Examples

Code examples here.

## License

MIT
```

### 2. Tutorial

**Purpose**: Teach a specific skill

```markdown
# How to Build X with Y

## Prerequisites
What readers need to know.

## Step 1: Setup
First step with code.

## Step 2: Core Logic
Main implementation.

## Step 3: Testing
How to verify it works.

## Conclusion
Summary and next steps.
```

### 3. Case Study

**Purpose**: Show problem-solving process

```markdown
# Solving X Problem

## Context
The situation and constraints.

## Approach
Why you chose this solution.

## Implementation
How you built it.

## Results
What you achieved.

## Lessons Learned
What you'd do differently.
```

### 4. Learning Reflection

**Purpose**: Process your learning

```markdown
# What I Learned Building X

## The Challenge
What was hard.

## Key Insights
Main takeaways.

## Mistakes Made
What went wrong.

## What's Next
Future plans.
```

---

## Writing Process

### 1. Capture While Fresh (10 min)

Immediately after finishing:
- Note key decisions
- Screenshot results
- Save error messages
- Write rough outline

### 2. Outline (15 min)

Structure your piece:
```
- Hook: Why should reader care?
- Context: What's the background?
- Content: What are you sharing?
- Conclusion: What's the takeaway?
```

### 3. Draft (30-60 min)

Write without editing:
- Get ideas down
- Don't worry about perfection
- Include code snippets
- Add placeholder for visuals

### 4. Edit (15-30 min)

Polish your draft:
- Cut unnecessary words
- Check code accuracy
- Add visuals
- Proofread

### 5. Publish (5 min)

- Choose platform
- Format for platform
- Add tags/categories
- Share

---

## Writing Tips

### Be Specific

**Bad**: "I learned a lot about Python."

**Good**: "I learned that list comprehensions are 30% faster than for loops for simple transformations."

### Show, Don't Tell

**Bad**: "The API is easy to use."

**Good**:
```python
response = api.predict(text="Hello world")
print(response.sentiment)  # "positive"
```

### Include Failures

Readers learn from mistakes:
> "My first approach using X failed because Y.
> I switched to Z which solved the problem."

### Use Visuals

- Screenshots of results
- Diagrams of architecture
- Code snippets with syntax highlighting
- Before/after comparisons

---

## Code in Write-Ups

### Good Code Examples

```python
# Clear and focused
def calculate_sentiment(text: str) -> float:
    """Return sentiment score from -1 to 1."""
    tokens = tokenize(text)
    return model.predict(tokens)
```

### Explain Complex Code

```python
# We use a sliding window to process the data
# because the full dataset doesn't fit in memory
for chunk in pd.read_csv('large.csv', chunksize=10000):
    process(chunk)
```

### Highlight Key Lines

```python
def train_model(data):
    model = create_model()
    # This is the key insight: using early stopping
    # prevents overfitting and saves training time
    model.fit(data, callbacks=[EarlyStopping(patience=3)])
    return model
```

---

## Templates

### Project README Template

```markdown
# Project Name

One-sentence description.

## Features

- Feature 1
- Feature 2

## Quick Start

git clone [url]
cd project
pip install -r requirements.txt
python main.py

## Documentation

See [docs/](docs/) for full documentation.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT
```

### Tutorial Template

```markdown
# How to [Accomplish Task]

In this tutorial, you'll learn to [outcome].

## Prerequisites

- Python 3.11+
- [Other requirements]

## What We're Building

[Screenshot or description]

## Step 1: [First Step]

[Explanation]

[Code]

## Step 2: [Second Step]

[Continue pattern]

## Complete Code

[Full working example]

## Next Steps

- Try [variation 1]
- Explore [related topic]

## Resources

- [Link 1]
- [Link 2]
```

### Reflection Template

```markdown
# Week X Reflection

## What I Built

[Brief description]

## What Went Well

- [Success 1]
- [Success 2]

## What Was Challenging

- [Challenge 1] - [How I solved it]
- [Challenge 2] - [How I solved it]

## Key Learnings

1. [Learning 1]
2. [Learning 2]

## Next Week

- [Goal 1]
- [Goal 2]
```

---

## Publishing Platforms

### GitHub

- Always publish code here
- Great README matters
- Add topics/tags
- Pin best projects

### Dev.to / Medium

- Longer tutorials
- Case studies
- Learning journeys
- Good for discovery

### Personal Blog

- Full control
- Portfolio showcase
- Custom domain
- SEO benefits

### LinkedIn

- Shorter posts
- Professional audience
- Career visibility
- Network building
