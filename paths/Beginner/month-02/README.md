# Month 02: Python Advanced

**Duration**: 4 weeks
**Focus**: Advanced Python features and best practices

---

## Objectives

By the end of this month, you will:

- [ ] Master object-oriented programming
- [ ] Use decorators and context managers
- [ ] Write unit tests with pytest
- [ ] Apply Python best practices
- [ ] Build an OOP-based project

---

## Weekly Breakdown

| Week | Focus | Deliverables |
|------|-------|--------------|
| Week 1 | Classes & Objects | OOP exercises |
| Week 2 | Decorators & Generators | Advanced patterns |
| Week 3 | Testing with pytest | Test suite |
| Week 4 | Project & Integration | Month project |

---

## Technologies

| Technology | Purpose |
|------------|---------|
| Python 3.11+ | Programming language |
| pytest | Testing framework |
| ruff | Linting |

---

## Project: Library Management System

Build an OOP-based library system that:

- Manages books (add, remove, search)
- Handles library members
- Tracks borrowing/returns
- Saves state to JSON

---

## Key Concepts

### Object-Oriented Programming

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"
```

### Decorators

```python
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper
```

### Testing

```python
def test_book_creation():
    book = Book("1984", "George Orwell", "123")
    assert book.title == "1984"
    assert book.is_available == True
```

---

## Getting Started

1. Review Month 01 concepts
2. Read Week 1 materials
3. Run `/plan-week` for weekly plan
