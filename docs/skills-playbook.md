# Skills Playbook

Step-by-step guides for common AI practitioner tasks.

## Available Skills

| Skill | Purpose | Time |
|-------|---------|------|
| [EDA to Insight](#eda-to-insight) | Explore data, find patterns | 2-3 hours |
| [Ship API](#ship-api) | Build and deploy an API | 2 hours |
| [Build RAG](#build-rag) | Create retrieval-augmented system | 2 hours |
| [Run Evals](#run-evals) | Evaluate model performance | 2 hours |

---

## EDA to Insight

Transform raw data into actionable insights.

### When to Use

- Starting a new data project
- Exploring unfamiliar data
- Looking for patterns
- Preparing for modeling

### Quick Steps

1. **Load and Look** (30 min)
   ```python
   import pandas as pd
   df = pd.read_csv('data.csv')
   df.head()
   df.info()
   df.describe()
   ```

2. **Check Quality** (30 min)
   - Missing values
   - Duplicates
   - Data types

3. **Univariate Analysis** (45 min)
   - Histograms for numeric
   - Value counts for categorical

4. **Bivariate Analysis** (45 min)
   - Correlation matrix
   - Scatter plots

5. **Document Insights** (30 min)
   - Key findings
   - Recommendations

### Deliverables

- [ ] Analysis notebook
- [ ] Key findings summary
- [ ] Visualizations
- [ ] Data quality report

Full details: [.claude/skills/eda-to-insight.md](../.claude/skills/eda-to-insight.md)

---

## Ship API

Build and deploy a production-ready API.

### When to Use

- Creating a web service
- Exposing ML models
- Building backends

### Quick Steps

1. **Setup** (15 min)
   ```bash
   mkdir my-api && cd my-api
   python -m venv venv
   source venv/bin/activate
   pip install flask pytest
   ```

2. **Core Implementation** (60 min)
   - Create `/health` endpoint
   - Create main endpoint
   - Add input validation

3. **Testing** (30 min)
   - Write unit tests
   - Test error cases

4. **Documentation** (15 min)
   - README with setup
   - API endpoint docs

5. **Verify** (15 min)
   - Run tests
   - Test with curl

### Deliverables

- [ ] Working API (2+ endpoints)
- [ ] Tests (80%+ coverage)
- [ ] README
- [ ] requirements.txt

Full details: [.claude/skills/ship-api.md](../.claude/skills/ship-api.md)

---

## Build RAG

Build a Retrieval-Augmented Generation system.

### When to Use

- Q&A over documents
- Knowledge-base chatbots
- Custom LLM data

### Quick Steps

1. **Prepare Documents** (30 min)
   - Load documents
   - Chunk text
   - Add metadata

2. **Index** (30 min)
   - Create embeddings (or TF-IDF)
   - Build search index

3. **Query Pipeline** (30 min)
   - Retrieve relevant chunks
   - Build prompt with context
   - (Send to LLM)

4. **Evaluate** (30 min)
   - Test with sample queries
   - Check relevance

### Deliverables

- [ ] Document chunking
- [ ] Retrieval system
- [ ] Query pipeline
- [ ] Test queries

Full details: [.claude/skills/build-rag.md](../.claude/skills/build-rag.md)

---

## Run Evals

Evaluate model or system performance systematically.

### When to Use

- Testing ML models
- Comparing approaches
- Regression testing

### Quick Steps

1. **Define Metrics** (20 min)
   - Choose appropriate metrics
   - Classification: accuracy, F1
   - Regression: MSE, MAE

2. **Create Test Dataset** (30 min)
   - Define test cases
   - Include edge cases
   - Save as JSON

3. **Run Evaluation** (30 min)
   - Run model on all cases
   - Collect predictions
   - Measure latency

4. **Analyze** (30 min)
   - Calculate metrics
   - Find failures
   - Generate report

5. **Track** (20 min)
   - Save results
   - Compare to baseline

### Deliverables

- [ ] Test dataset
- [ ] Evaluation script
- [ ] Results analysis
- [ ] Performance report

Full details: [.claude/skills/run-evals.md](../.claude/skills/run-evals.md)

---

## Using Skills

### From Claude Code

Ask Claude to guide you through a skill:

```
I want to do EDA on my sales data.
Can you walk me through the EDA to Insight skill?
```

### Self-Directed

Open the skill file and follow step-by-step:

1. Read the skill in `.claude/skills/`
2. Work through each phase
3. Check off deliverables
4. Log completion in journal

### Combining Skills

Skills often chain together:

1. **EDA to Insight** → Understand your data
2. **Ship API** → Expose your model
3. **Run Evals** → Test performance
4. **Build RAG** → Add document context

---

## Adding New Skills

Create new skills in `.claude/skills/`:

```markdown
# Skill: [Name]

[Description of the skill]

## When to Use

- [Situation 1]
- [Situation 2]

## Playbook

### Phase 1: [Name] (Time)

[Steps and code]

### Phase 2: [Name] (Time)

[Steps and code]

## Deliverables

- [ ] Deliverable 1
- [ ] Deliverable 2

## Tips

- Tip 1
- Tip 2
```
