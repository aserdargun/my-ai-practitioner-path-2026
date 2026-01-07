# Month 07: Machine Learning Basics

**Duration**: 4 weeks
**Focus**: Introduction to machine learning

---

## Objectives

By the end of this month, you will:

- [ ] Understand ML fundamentals
- [ ] Prepare data for ML models
- [ ] Train classification and regression models
- [ ] Evaluate model performance
- [ ] Build a predictive model

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | ML Concepts | Understanding fundamentals |
| Week 2 | Classification | Classifier model |
| Week 3 | Regression | Regression model |
| Week 4 | Project | End-to-end ML project |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Scikit-learn | ML library |
| Pandas | Data preparation |
| Matplotlib | Visualization |

---

## Project: Housing Price Predictor

Build a model that:

- Loads and prepares housing data
- Trains a regression model
- Evaluates performance
- Makes predictions

---

## Key Concepts

### ML Workflow

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
```

### Key Metrics

| Task | Metrics |
|------|---------|
| Classification | Accuracy, Precision, Recall, F1 |
| Regression | MSE, RMSE, MAE, R² |
