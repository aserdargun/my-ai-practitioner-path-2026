# Skill: EDA to Insight

Transform raw data into actionable insights through exploratory data analysis.

## When to Use

- Starting a new data analysis project
- Exploring an unfamiliar dataset
- Looking for patterns and anomalies
- Preparing data for modeling

## Playbook

### Phase 1: Data Loading and First Look (30 min)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data.csv')

# First look
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
df.head()
df.info()
df.describe()
```

### Phase 2: Data Quality Check (30 min)

```python
# Missing values
missing = df.isnull().sum()
missing_pct = (missing / len(df)) * 100
print("Missing Values:")
print(missing_pct[missing_pct > 0])

# Duplicates
duplicates = df.duplicated().sum()
print(f"Duplicates: {duplicates}")

# Data types
print(df.dtypes)
```

### Phase 3: Univariate Analysis (45 min)

```python
# Numeric columns
numeric_cols = df.select_dtypes(include=[np.number]).columns

for col in numeric_cols:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    df[col].hist(ax=axes[0])
    axes[0].set_title(f'{col} - Distribution')
    df.boxplot(column=col, ax=axes[1])
    axes[1].set_title(f'{col} - Boxplot')
    plt.tight_layout()
    plt.show()

# Categorical columns
cat_cols = df.select_dtypes(include=['object']).columns

for col in cat_cols:
    print(f"\n{col}:")
    print(df[col].value_counts())
```

### Phase 4: Bivariate Analysis (45 min)

```python
# Correlation matrix
corr = df[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Scatter plots for high correlations
for i, col1 in enumerate(numeric_cols):
    for col2 in numeric_cols[i+1:]:
        if abs(corr.loc[col1, col2]) > 0.5:
            plt.scatter(df[col1], df[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)
            plt.title(f'{col1} vs {col2}')
            plt.show()
```

### Phase 5: Document Insights (30 min)

Create a summary with:
1. Key statistics
2. Data quality issues found
3. Notable patterns
4. Recommendations for next steps

## Deliverables

- [ ] Jupyter notebook with analysis
- [ ] Summary of key findings
- [ ] Visualization exports
- [ ] Data quality report

## Tips

- Always look at raw data first
- Question outliers - are they errors or real?
- Document assumptions
- Save cleaned data separately
