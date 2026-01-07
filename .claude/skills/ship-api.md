# Skill: Ship API

Build and deploy a production-ready API.

## When to Use

- Creating a web service
- Exposing ML models via API
- Building backend for applications

## Playbook

### Phase 1: Project Setup (15 min)

```bash
# Create project structure
mkdir my-api && cd my-api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install flask pytest
pip freeze > requirements.txt
```

```
my-api/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── tests/
│   └── test_routes.py
├── requirements.txt
└── README.md
```

### Phase 2: Core Implementation (60 min)

```python
# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.routes import bp
    app.register_blueprint(bp)

    return app

# app/routes.py
from flask import Blueprint, jsonify, request

bp = Blueprint('api', __name__)

@bp.route('/health')
def health():
    return jsonify({'status': 'healthy'})

@bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    if not data or 'input' not in data:
        return jsonify({'error': 'Missing input'}), 400

    # Your logic here
    result = process(data['input'])

    return jsonify({'result': result})
```

### Phase 3: Testing (30 min)

```python
# tests/test_routes.py
import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_predict_missing_input(client):
    response = client.post('/predict', json={})
    assert response.status_code == 400

def test_predict_success(client):
    response = client.post('/predict', json={'input': 'test'})
    assert response.status_code == 200
    assert 'result' in response.json
```

### Phase 4: Documentation (15 min)

```markdown
# My API

## Setup
pip install -r requirements.txt

## Run
flask run

## Endpoints

### GET /health
Health check endpoint.

### POST /predict
Make a prediction.

Request:
{
    "input": "your data here"
}

Response:
{
    "result": "prediction result"
}
```

### Phase 5: Run and Verify (15 min)

```bash
# Run tests
pytest

# Run server
flask run

# Test with curl
curl http://localhost:5000/health
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"input": "test"}'
```

## Deliverables

- [ ] Working API with at least 2 endpoints
- [ ] Tests with 80%+ coverage
- [ ] README with setup and usage
- [ ] requirements.txt with pinned versions

## Tips

- Start with `/health` endpoint
- Add input validation early
- Test error cases
- Use environment variables for config
