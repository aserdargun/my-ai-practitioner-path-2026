# Month 10: Time Series Analysis

**Duration**: 4 weeks
**Focus**: Time series data and forecasting

---

## Objectives

By the end of this month, you will:

- [ ] Work with datetime data
- [ ] Understand time series components
- [ ] Apply decomposition and analysis
- [ ] Build forecasting models
- [ ] Create a forecasting application

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | DateTime & Time Series | Data preparation |
| Week 2 | Analysis & Decomposition | Component analysis |
| Week 3 | Forecasting Models | Prediction model |
| Week 4 | Project | Forecasting app |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Pandas | Time series handling |
| statsmodels | Statistical models |
| Matplotlib | Visualization |

---

## Project: Sales Forecaster

Build a sales forecasting system:

- Analyze historical sales
- Identify trends and seasonality
- Train forecasting model
- Generate predictions

---

## Key Concepts

### Time Series Basics

```python
import pandas as pd

df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Resample to monthly
monthly = df.resample('M').sum()

# Rolling average
df['rolling_mean'] = df['sales'].rolling(window=7).mean()
```

### Decomposition

```python
from statsmodels.tsa.seasonal import seasonal_decompose

decomposition = seasonal_decompose(df['sales'], model='additive', period=12)
decomposition.plot()
```

### Forecasting

```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

model = ExponentialSmoothing(
    train['sales'],
    seasonal='add',
    seasonal_periods=12
)
fitted = model.fit()
forecast = fitted.forecast(12)
```
