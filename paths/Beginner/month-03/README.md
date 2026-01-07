# Month 03: Data Analysis with Pandas

**Duration**: 4 weeks
**Focus**: Data manipulation and analysis

---

## Objectives

By the end of this month, you will:

- [ ] Load and explore datasets
- [ ] Clean and transform data
- [ ] Perform aggregations and grouping
- [ ] Merge and join datasets
- [ ] Complete an EDA project

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | DataFrames Basics | Load and explore data |
| Week 2 | Data Cleaning | Handle missing values, types |
| Week 3 | Aggregation & Grouping | Summary statistics |
| Week 4 | EDA Project | Complete analysis |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Jupyter | Interactive analysis |

---

## Project: Sales Data Analysis

Analyze a retail sales dataset to:

- Clean and prepare data
- Calculate key metrics
- Identify trends
- Generate insights report

---

## Key Concepts

### DataFrames

```python
import pandas as pd

df = pd.read_csv("sales.csv")
df.head()
df.info()
df.describe()
```

### Cleaning

```python
df.dropna()
df.fillna(0)
df['date'] = pd.to_datetime(df['date'])
```

### Aggregation

```python
df.groupby('category')['sales'].sum()
df.pivot_table(values='sales', index='month', columns='product')
```

---

## Skill: EDA to Insight

Use the [EDA to Insight](../../../.claude/skills/eda-to-insight.md) skill playbook for this month's project.
