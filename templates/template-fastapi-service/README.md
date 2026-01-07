# FastAPI Service Template

A production-ready template for building FastAPI services.

## Structure

```
template-fastapi-service/
├── app/
│   ├── __init__.py
│   ├── main.py         # Application entry point
│   ├── routes.py       # API endpoints
│   ├── models.py       # Pydantic models
│   └── config.py       # Configuration
├── tests/
│   ├── __init__.py
│   └── test_routes.py  # API tests
├── requirements.txt    # Dependencies
├── pyproject.toml      # Project config
└── README.md           # This file
```

## Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload

# Run tests
pytest
```

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/health` | Detailed health |
| POST | `/predict` | Make prediction |

## Customizing

1. Add your models to `app/models.py`
2. Add routes to `app/routes.py`
3. Update tests in `tests/test_routes.py`

## Configuration

Set environment variables:
- `DEBUG`: Enable debug mode
- `API_KEY`: Optional API key

## Testing

```bash
pytest -v
pytest --cov=app
```
