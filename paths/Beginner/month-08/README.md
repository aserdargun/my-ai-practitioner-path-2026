# Month 08: ML Pipelines

**Duration**: 4 weeks
**Focus**: Production-ready ML workflows

---

## Objectives

By the end of this month, you will:

- [ ] Build end-to-end ML pipelines
- [ ] Handle feature engineering
- [ ] Implement cross-validation
- [ ] Save and load models
- [ ] Create a complete ML pipeline

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | Feature Engineering | Feature pipeline |
| Week 2 | Pipelines & Validation | Sklearn pipelines |
| Week 3 | Model Persistence | Save/load models |
| Week 4 | Project | Complete pipeline |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Scikit-learn | ML library |
| joblib | Model serialization |
| pandas | Data processing |

---

## Project: Customer Churn Pipeline

Build an ML pipeline that:

- Preprocesses customer data
- Trains a churn classifier
- Evaluates with cross-validation
- Saves model for deployment

---

## Key Concepts

### Sklearn Pipelines

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier())
])

pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)
```

### Cross-Validation

```python
from sklearn.model_selection import cross_val_score

scores = cross_val_score(pipeline, X, y, cv=5)
print(f"Average accuracy: {scores.mean():.2f}")
```

### Model Persistence

```python
import joblib

# Save
joblib.dump(pipeline, 'model.pkl')

# Load
loaded = joblib.load('model.pkl')
predictions = loaded.predict(new_data)
```
