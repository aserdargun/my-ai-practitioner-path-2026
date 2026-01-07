# How to Demo Your Work

A guide to presenting and demonstrating your projects.

## Why Demo?

- Solidifies your understanding
- Builds communication skills
- Creates portfolio pieces
- Gets feedback
- Celebrates progress

## Demo Checklist

Before demoing, ensure:

- [ ] Code works end-to-end
- [ ] Tests pass
- [ ] README has setup instructions
- [ ] Demo script prepared
- [ ] Error cases handled
- [ ] `/publish` check passes

---

## Preparing Your Demo

### 1. Define Your Story (15 min)

Answer these questions:

- **What problem does this solve?**
- **Who would use this?**
- **What's the key feature?**
- **What did you learn?**

### 2. Create Demo Script (30 min)

Structure your demo:

```
1. Hook (30 sec)
   "Have you ever struggled with X? I built Y to solve it."

2. Problem (1 min)
   Show the pain point.

3. Solution (2-3 min)
   Demo the working feature.

4. How It Works (1-2 min)
   Quick code walkthrough.

5. What I Learned (1 min)
   Key takeaways.

6. Next Steps (30 sec)
   Future improvements.
```

### 3. Practice (15 min)

- Run through once solo
- Time yourself
- Anticipate questions
- Prepare for failures

---

## Demo Formats

### Live Demo

**Best for**: Working software, APIs, UIs

```bash
# Example: API demo
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product!"}'

# Show the response
{"sentiment": "positive", "score": 0.92}
```

### Walkthrough

**Best for**: Data analysis, notebooks

- Open Jupyter notebook
- Walk through cells
- Show visualizations
- Explain insights

### Recorded Video

**Best for**: Complex setups, async sharing

Tools:
- OBS Studio (free)
- Loom
- QuickTime

Tips:
- Keep under 5 minutes
- Show, don't tell
- Edit out mistakes

---

## Common Demo Scenarios

### API Demo

```bash
# 1. Show the health check
curl http://localhost:5000/health
{"status": "healthy"}

# 2. Show the main feature
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{"data": [1, 2, 3, 4, 5]}'

# 3. Show error handling
curl -X POST http://localhost:5000/analyze \
  -H "Content-Type: application/json" \
  -d '{}'
{"error": "Missing data field"}
```

### Data Analysis Demo

```python
# 1. Show the data
df.head()

# 2. Show key insight
df.groupby('category')['sales'].mean().plot(kind='bar')

# 3. Show the takeaway
print(f"Category A outperforms by {improvement}%")
```

### ML Model Demo

```python
# 1. Load the model
model = load_model('model.pkl')

# 2. Make a prediction
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)
print(f"Predicted: {prediction[0]}")

# 3. Show performance
print(f"Accuracy: {accuracy:.2%}")
```

---

## Handling Demo Failures

### Prevention

- Test everything before demo
- Have backup screenshots
- Know your recovery path

### During Failure

1. Stay calm
2. Acknowledge briefly
3. Explain what should happen
4. Move on or show backup

**Example**:
> "Interesting! That's not what usually happens.
> Normally you'd see X. Let me show you a backup..."

---

## Writing About Your Work

### Blog Post Structure

```markdown
# [Catchy Title]

## The Problem
What challenge did you tackle?

## The Solution
What did you build?

## How It Works
Key technical details.

## Results
What did you achieve?

## What I Learned
Key takeaways.

## Try It Yourself
Link to code, demo.
```

### README for Portfolio

```markdown
# Project Name

One-line description.

## Demo
[Screenshot or GIF]

## Quick Start
pip install -r requirements.txt
python app.py

## Features
- Feature 1
- Feature 2

## Built With
- Python
- Flask
- pandas
```

---

## Sharing Your Work

### Where to Share

- GitHub (always)
- LinkedIn (professional)
- Twitter/X (tech community)
- Dev.to / Medium (written)
- YouTube (video)

### GitHub README Tips

- Add badges (build status, coverage)
- Include screenshot/GIF
- Clear setup instructions
- Link to demo if hosted

### LinkedIn Post Format

```
🚀 Just shipped: [Project Name]

Problem: [One sentence]
Solution: [One sentence]
Built with: [Tech stack]

[1-2 key learnings]

Link: [GitHub URL]

#Python #DataScience #LearningInPublic
```

---

## Using /publish Command

Before sharing, run:

```
/publish
```

This checks:
- All changes committed
- Tests passing
- No TODO comments
- README exists
- No debug code

Only share after checks pass!
