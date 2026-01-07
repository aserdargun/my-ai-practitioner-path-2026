# Week 3: Functions & Modules

**Focus**: Writing reusable code with functions and modules

---

## Objectives

- [ ] Define and call functions
- [ ] Use parameters and return values
- [ ] Handle errors with try/except
- [ ] Import and use modules
- [ ] Write your own module

---

## Tasks

### Day 1-2: Functions Basics

1. **Defining Functions**
   ```python
   def greet(name):
       """Say hello to someone."""
       return f"Hello, {name}!"

   message = greet("Alice")
   print(message)  # Hello, Alice!
   ```

2. **Multiple Parameters**
   ```python
   def add(a, b):
       """Add two numbers."""
       return a + b

   def describe_person(name, age, city="Unknown"):
       """Describe a person."""
       return f"{name} is {age} years old from {city}"

   print(add(5, 3))  # 8
   print(describe_person("Bob", 25))  # Bob is 25 years old from Unknown
   print(describe_person("Alice", 30, "NYC"))  # Alice is 30 years old from NYC
   ```

3. **Default and Keyword Arguments**
   ```python
   def power(base, exponent=2):
       """Calculate base raised to exponent."""
       return base ** exponent

   print(power(3))         # 9 (3^2)
   print(power(3, 3))      # 27 (3^3)
   print(power(exponent=4, base=2))  # 16 (2^4)
   ```

### Day 3: Error Handling

1. **Try/Except**
   ```python
   def divide(a, b):
       """Safely divide two numbers."""
       try:
           result = a / b
           return result
       except ZeroDivisionError:
           return "Cannot divide by zero!"
       except TypeError:
           return "Please provide numbers!"

   print(divide(10, 2))   # 5.0
   print(divide(10, 0))   # Cannot divide by zero!
   print(divide(10, "a")) # Please provide numbers!
   ```

2. **Raising Exceptions**
   ```python
   def validate_age(age):
       """Validate that age is positive."""
       if age < 0:
           raise ValueError("Age cannot be negative")
       return age

   try:
       validate_age(-5)
   except ValueError as e:
       print(f"Error: {e}")
   ```

### Day 4-5: Modules

1. **Importing Modules**
   ```python
   # Import entire module
   import math
   print(math.sqrt(16))  # 4.0
   print(math.pi)        # 3.14159...

   # Import specific functions
   from math import sqrt, pi
   print(sqrt(16))  # 4.0

   # Import with alias
   import datetime as dt
   print(dt.datetime.now())
   ```

2. **Create Your Own Module**

   Create `utils.py`:
   ```python
   """Utility functions for our projects."""

   def clean_text(text):
       """Remove extra whitespace and lowercase."""
       return " ".join(text.lower().split())

   def is_valid_email(email):
       """Basic email validation."""
       return "@" in email and "." in email
   ```

   Use in `main.py`:
   ```python
   from utils import clean_text, is_valid_email

   text = "  Hello   World  "
   print(clean_text(text))  # "hello world"

   print(is_valid_email("test@example.com"))  # True
   print(is_valid_email("invalid"))           # False
   ```

---

## Exercises

### Exercise 1: Temperature Converter

```python
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Test
print(celsius_to_fahrenheit(0))    # 32.0
print(celsius_to_fahrenheit(100))  # 212.0
print(fahrenheit_to_celsius(98.6)) # 37.0
```

### Exercise 2: List Statistics

```python
def list_stats(numbers):
    """Calculate statistics for a list of numbers."""
    if not numbers:
        return None

    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "average": sum(numbers) / len(numbers)
    }

# Test
data = [10, 20, 30, 40, 50]
stats = list_stats(data)
print(stats)
```

### Exercise 3: Safe File Reader

```python
def read_file_safely(filepath):
    """Read a file, handling errors gracefully."""
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"File not found: {filepath}"
    except PermissionError:
        return f"Permission denied: {filepath}"
    except Exception as e:
        return f"Error reading file: {e}"
```

---

## Checklist

- [ ] Defined functions with parameters
- [ ] Used return values
- [ ] Implemented default arguments
- [ ] Added error handling with try/except
- [ ] Imported standard library modules
- [ ] Created and used a custom module
- [ ] Completed all exercises
- [ ] Wrote week 3 journal entry

---

## Reflection Prompt

*How do functions help make code more maintainable? Think of a task from your daily life that could be broken into functions.*

---

## Next

Proceed to [Week 4](week-4.md) for file I/O and the month project.
