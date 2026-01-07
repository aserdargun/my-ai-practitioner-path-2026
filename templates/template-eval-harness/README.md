# Evaluation Harness Template

A template for systematic model/system evaluation.

## Structure

```
template-eval-harness/
├── eval/
│   ├── __init__.py
│   ├── dataset.py      # Test dataset handling
│   ├── metrics.py      # Evaluation metrics
│   ├── runner.py       # Evaluation runner
│   └── report.py       # Report generation
├── tests/
│   └── test_eval.py
├── data/
│   └── eval_dataset.json
├── requirements.txt
└── README.md
```

## Quick Start

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run evaluation
python -m eval.runner --dataset data/eval_dataset.json

# Run tests
pytest
```

## Usage

```python
from eval.runner import EvaluationRunner

# Your model function
def my_model(input_text):
    return "prediction"

# Run evaluation
runner = EvaluationRunner(model_fn=my_model)
results = runner.evaluate("data/eval_dataset.json")
print(results.summary())
```
