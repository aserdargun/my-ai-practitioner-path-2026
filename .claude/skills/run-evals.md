# Skill: Run Evals

Evaluate model or system performance systematically.

## When to Use

- Testing ML model performance
- Comparing approaches
- Validating system behavior
- Regression testing

## Playbook

### Phase 1: Define Metrics (20 min)

```python
# Common metrics
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    mean_squared_error,
    mean_absolute_error
)

# Classification metrics
def classification_metrics(y_true, y_pred):
    return {
        'accuracy': accuracy_score(y_true, y_pred),
        'precision': precision_score(y_true, y_pred, average='weighted'),
        'recall': recall_score(y_true, y_pred, average='weighted'),
        'f1': f1_score(y_true, y_pred, average='weighted')
    }

# Regression metrics
def regression_metrics(y_true, y_pred):
    return {
        'mse': mean_squared_error(y_true, y_pred),
        'mae': mean_absolute_error(y_true, y_pred),
        'rmse': mean_squared_error(y_true, y_pred, squared=False)
    }
```

### Phase 2: Create Test Dataset (30 min)

```python
import json

# Define test cases
test_cases = [
    {
        'id': 'test_001',
        'input': 'sample input 1',
        'expected': 'expected output 1',
        'category': 'basic'
    },
    {
        'id': 'test_002',
        'input': 'sample input 2',
        'expected': 'expected output 2',
        'category': 'edge_case'
    }
]

# Save test dataset
with open('eval_dataset.json', 'w') as f:
    json.dump(test_cases, f, indent=2)
```

### Phase 3: Run Evaluation (30 min)

```python
import json
from datetime import datetime

def run_evaluation(model_fn, test_cases):
    """Run model on all test cases."""
    results = []

    for case in test_cases:
        start_time = datetime.now()
        prediction = model_fn(case['input'])
        end_time = datetime.now()

        results.append({
            'id': case['id'],
            'input': case['input'],
            'expected': case['expected'],
            'predicted': prediction,
            'correct': prediction == case['expected'],
            'latency_ms': (end_time - start_time).total_seconds() * 1000,
            'category': case['category']
        })

    return results

# Example model function
def my_model(input_text):
    # Your model logic here
    return "prediction"

# Run evaluation
results = run_evaluation(my_model, test_cases)
```

### Phase 4: Analyze Results (30 min)

```python
import pandas as pd

def analyze_results(results):
    """Generate evaluation report."""
    df = pd.DataFrame(results)

    report = {
        'total_cases': len(df),
        'correct': df['correct'].sum(),
        'accuracy': df['correct'].mean(),
        'avg_latency_ms': df['latency_ms'].mean(),
        'by_category': df.groupby('category')['correct'].mean().to_dict()
    }

    # Find failures
    failures = df[~df['correct']]
    report['failures'] = failures[['id', 'input', 'expected', 'predicted']].to_dict('records')

    return report

report = analyze_results(results)
print(json.dumps(report, indent=2))
```

### Phase 5: Document and Track (20 min)

```python
# Save evaluation run
eval_record = {
    'timestamp': datetime.now().isoformat(),
    'model_version': 'v1.0',
    'dataset': 'eval_dataset.json',
    'metrics': report
}

# Append to eval history
with open('eval_history.jsonl', 'a') as f:
    f.write(json.dumps(eval_record) + '\n')
```

## Deliverables

- [ ] Test dataset with diverse cases
- [ ] Evaluation script
- [ ] Results analysis
- [ ] Performance report
- [ ] Tracking over time

## Tips

- Include edge cases in test set
- Track latency alongside accuracy
- Version your test datasets
- Compare against baseline
