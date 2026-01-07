# Data Pipeline Template

A template for building ETL/data processing pipelines.

## Structure

```
template-data-pipeline/
├── pipeline/
│   ├── __init__.py
│   ├── extract.py      # Data extraction
│   ├── transform.py    # Data transformation
│   ├── load.py         # Data loading
│   └── run.py          # Pipeline orchestration
├── tests/
│   └── test_pipeline.py
├── data/
│   ├── raw/            # Raw input data
│   └── processed/      # Processed output
├── requirements.txt
└── README.md
```

## Quick Start

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run the pipeline
python -m pipeline.run

# Run tests
pytest
```

## Usage

```python
from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.load import load_data

# Run ETL
raw_data = extract_data("data/raw/input.csv")
processed = transform_data(raw_data)
load_data(processed, "data/processed/output.csv")
```
