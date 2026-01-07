# Week 4: Files & Project

**Focus**: File operations and completing the month project

---

## Objectives

- [ ] Read and write text files
- [ ] Work with JSON files
- [ ] Handle file paths properly
- [ ] Complete the expense tracker project
- [ ] Write month-end reflection

---

## Tasks

### Day 1-2: File Operations

1. **Reading Files**
   ```python
   # Read entire file
   with open("data.txt", "r") as f:
       content = f.read()
       print(content)

   # Read line by line
   with open("data.txt", "r") as f:
       for line in f:
           print(line.strip())

   # Read all lines into list
   with open("data.txt", "r") as f:
       lines = f.readlines()
   ```

2. **Writing Files**
   ```python
   # Write (overwrite)
   with open("output.txt", "w") as f:
       f.write("Hello, World!\n")
       f.write("Second line\n")

   # Append
   with open("output.txt", "a") as f:
       f.write("Appended line\n")
   ```

3. **Working with JSON**
   ```python
   import json

   # Write JSON
   data = {
       "name": "Alice",
       "scores": [85, 90, 92]
   }
   with open("data.json", "w") as f:
       json.dump(data, f, indent=2)

   # Read JSON
   with open("data.json", "r") as f:
       loaded = json.load(f)
       print(loaded["name"])  # Alice
   ```

### Day 3-5: Complete Project

Build the **Expense Tracker**!

See [project/README.md](project/README.md) for full requirements.

**Core Features**:
1. Add an expense (date, category, amount, description)
2. Save expenses to JSON file
3. Load expenses from file
4. View all expenses
5. Summary by category

**Project Structure**:
```
project/
├── expense_tracker.py   # Main application
├── expenses.json        # Data file
└── README.md            # Project documentation
```

---

## Exercises

### Exercise 1: Log Writer

```python
from datetime import datetime

def log_message(message, filename="app.log"):
    """Write a timestamped message to a log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open(filename, "a") as f:
        f.write(log_entry)

# Test
log_message("Application started")
log_message("User logged in")
log_message("Error occurred", "error.log")
```

### Exercise 2: Config Manager

```python
import json

def load_config(filepath="config.json"):
    """Load configuration from JSON file."""
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_config(config, filepath="config.json"):
    """Save configuration to JSON file."""
    with open(filepath, "w") as f:
        json.dump(config, f, indent=2)

# Test
config = load_config()
config["theme"] = "dark"
config["font_size"] = 14
save_config(config)
```

### Exercise 3: CSV Reader

```python
def read_csv_simple(filepath):
    """Read a CSV file into a list of dictionaries."""
    with open(filepath, "r") as f:
        lines = f.readlines()

    if not lines:
        return []

    headers = lines[0].strip().split(",")
    data = []

    for line in lines[1:]:
        values = line.strip().split(",")
        row = dict(zip(headers, values))
        data.append(row)

    return data

# Test with a sample CSV
# name,age,city
# Alice,30,NYC
# Bob,25,LA
```

---

## Project Checklist

- [ ] Can add expenses
- [ ] Saves to JSON file
- [ ] Loads from JSON file
- [ ] Shows expense list
- [ ] Shows category summary
- [ ] Handles errors gracefully
- [ ] Has README with instructions
- [ ] Code is clean and commented

---

## Month 01 Checklist

- [ ] All week tasks completed
- [ ] Expense tracker project done
- [ ] At least 10 commits this month
- [ ] Journal entries for each week
- [ ] Month-end retrospective written

---

## Reflection Prompts

**Week 4**: *What was the hardest part of the project? How did you solve it?*

**Month 01**: *Looking back at the month, what are you most proud of? What would you do differently?*

---

## Month Complete!

Congratulations on completing Month 01!

**Next Steps**:
1. Run `/evaluate` for your month assessment
2. Write your month-end retrospective
3. Proceed to [Month 02](../month-02/README.md)
