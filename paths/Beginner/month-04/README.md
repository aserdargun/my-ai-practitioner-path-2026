# Month 04: Data Visualization

**Duration**: 4 weeks
**Focus**: Creating effective visualizations

---

## Objectives

By the end of this month, you will:

- [ ] Create charts with Matplotlib
- [ ] Build statistical plots with Seaborn
- [ ] Make interactive dashboards with Streamlit
- [ ] Apply visualization best practices
- [ ] Build a data dashboard

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | Matplotlib Basics | Basic charts |
| Week 2 | Seaborn & Statistics | Statistical plots |
| Week 3 | Streamlit | Interactive app |
| Week 4 | Dashboard Project | Complete dashboard |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Matplotlib | Basic plotting |
| Seaborn | Statistical visualization |
| Streamlit | Interactive dashboards |

---

## Project: Interactive Dashboard

Build a Streamlit dashboard that:

- Loads and displays data
- Shows multiple chart types
- Has interactive filters
- Provides insights summary

---

## Key Concepts

### Matplotlib

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['sales'])
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()
```

### Seaborn

```python
import seaborn as sns

sns.heatmap(df.corr(), annot=True)
sns.boxplot(x='category', y='sales', data=df)
sns.histplot(df['price'], kde=True)
```

### Streamlit

```python
import streamlit as st

st.title("Sales Dashboard")
st.line_chart(df['sales'])
category = st.selectbox("Category", df['category'].unique())
```
