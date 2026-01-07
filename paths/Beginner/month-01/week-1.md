# Week 1: Setup & Basics

**Focus**: Development environment and Python basics

---

## Objectives

- [ ] Install Python 3.11+
- [ ] Set up VS Code with Python extension
- [ ] Configure Git and create first repo
- [ ] Write and run your first Python script
- [ ] Understand basic syntax

---

## Tasks

### Day 1-2: Environment Setup

1. **Install Python**
   ```bash
   # Verify installation
   python --version
   # Should show Python 3.11.x or higher
   ```

2. **Install VS Code**
   - Download from [code.visualstudio.com](https://code.visualstudio.com)
   - Install Python extension

3. **Configure Git**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your@email.com"
   ```

### Day 3-4: Python Basics

1. **Create first script** (`hello.py`)
   ```python
   # My first Python script
   print("Hello, World!")

   # Variables
   name = "AI Learner"
   year = 2026

   print(f"Welcome, {name}! It's {year}.")
   ```

2. **Practice exercises**
   - Variable assignment
   - Basic math operations
   - String formatting

### Day 5: Git Practice

1. **Initialize repo**
   ```bash
   mkdir python-practice
   cd python-practice
   git init
   ```

2. **First commit**
   ```bash
   git add .
   git commit -m "Initial commit: hello.py"
   ```

---

## Exercises

### Exercise 1: Calculator

Create `calculator.py`:
```python
# Simple calculator
a = 10
b = 3

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
```

### Exercise 2: Personal Info

Create `about_me.py`:
```python
# Store your info in variables
name = "Your Name"
age = 25
city = "Your City"
learning_goal = "Become an AI practitioner"

# Print formatted output
print(f"Name: {name}")
print(f"Age: {age}")
print(f"City: {city}")
print(f"Goal: {learning_goal}")
```

---

## Checklist

- [ ] Python installed and working
- [ ] VS Code set up with Python extension
- [ ] Git configured
- [ ] Created and ran hello.py
- [ ] Completed calculator exercise
- [ ] Completed about_me exercise
- [ ] Made at least 2 commits
- [ ] Wrote week 1 journal entry

---

## Reflection Prompt

*What was your first impression of Python? How does it compare to any other programming you've done?*

---

## Next

Proceed to [Week 2](week-2.md) for data types and control flow.
