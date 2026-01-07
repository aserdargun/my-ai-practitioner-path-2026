# Month 06: Web APIs with Flask

**Duration**: 4 weeks
**Focus**: Building REST APIs

---

## Objectives

By the end of this month, you will:

- [ ] Understand HTTP and REST principles
- [ ] Build APIs with Flask
- [ ] Handle JSON requests/responses
- [ ] Add error handling and validation
- [ ] Deploy a simple API

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | HTTP & REST Basics | Simple endpoints |
| Week 2 | Flask Deep Dive | CRUD API |
| Week 3 | Testing & Error Handling | Robust API |
| Week 4 | Project & Deployment | Deployed API |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Flask | Web framework |
| requests | API testing |
| pytest | Testing |

---

## Project: Todo API

Build a RESTful Todo API with:

- CRUD endpoints
- JSON data storage
- Input validation
- Error handling
- API documentation

---

## Key Concepts

### Flask Basics

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'POST':
        data = request.get_json()
        # Add todo logic
        return jsonify({"created": True}), 201
    return jsonify({"todos": []})
```

### REST Principles

| Method | Endpoint | Action |
|--------|----------|--------|
| GET | /todos | List all |
| POST | /todos | Create |
| GET | /todos/:id | Get one |
| PUT | /todos/:id | Update |
| DELETE | /todos/:id | Delete |

---

## Skill: Ship API

Use the [Ship API](../../../.claude/skills/ship-api.md) skill playbook for this month's project.
