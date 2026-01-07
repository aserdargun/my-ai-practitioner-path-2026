# Expense Tracker Project

A command-line expense tracking application.

## Features

- Add expenses with date, category, amount, and description
- Save expenses to a JSON file
- Load expenses from file
- View all expenses
- View summary by category

## Usage

```bash
python expense_tracker.py
```

## Commands

| Command | Description |
|---------|-------------|
| `add` | Add a new expense |
| `list` | Show all expenses |
| `summary` | Show spending by category |
| `save` | Save to file |
| `load` | Load from file |
| `quit` | Exit the application |

## Example Session

```
Expense Tracker
===============

> add
Date (YYYY-MM-DD): 2026-01-15
Category: Food
Amount: 25.50
Description: Lunch with team

Expense added!

> add
Date (YYYY-MM-DD): 2026-01-15
Category: Transport
Amount: 15.00
Description: Uber ride

Expense added!

> list
2026-01-15 | Food      | $25.50 | Lunch with team
2026-01-15 | Transport | $15.00 | Uber ride

> summary
Category Summary:
Food:      $25.50
Transport: $15.00
-----------------
Total:     $40.50

> save
Saved 2 expenses to expenses.json

> quit
Goodbye!
```

## Project Structure

```
project/
├── expense_tracker.py   # Main application
├── expenses.json        # Data file (created on save)
└── README.md            # This file
```

## Requirements

- Python 3.11+
- No external dependencies (uses only stdlib)

## Implementation Guide

### Step 1: Data Structure

```python
# Each expense is a dictionary
expense = {
    "date": "2026-01-15",
    "category": "Food",
    "amount": 25.50,
    "description": "Lunch with team"
}

# All expenses in a list
expenses = []
```

### Step 2: Core Functions

```python
def add_expense(expenses, date, category, amount, description):
    """Add a new expense to the list."""
    pass

def list_expenses(expenses):
    """Print all expenses."""
    pass

def category_summary(expenses):
    """Print spending by category."""
    pass

def save_expenses(expenses, filename):
    """Save expenses to JSON file."""
    pass

def load_expenses(filename):
    """Load expenses from JSON file."""
    pass
```

### Step 3: Main Loop

```python
def main():
    expenses = []

    while True:
        command = input("> ").strip().lower()

        if command == "add":
            # Get input and add expense
            pass
        elif command == "list":
            list_expenses(expenses)
        elif command == "summary":
            category_summary(expenses)
        elif command == "save":
            save_expenses(expenses, "expenses.json")
        elif command == "load":
            expenses = load_expenses("expenses.json")
        elif command == "quit":
            print("Goodbye!")
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
```

## Stretch Goals

If you finish early, try adding:

- [ ] Edit an existing expense
- [ ] Delete an expense
- [ ] Filter by date range
- [ ] Filter by category
- [ ] Monthly spending report
- [ ] Export to CSV

## Evaluation Criteria

| Criteria | Points |
|----------|--------|
| Basic functionality works | 40 |
| Saves/loads correctly | 20 |
| Error handling | 15 |
| Code organization | 15 |
| Documentation | 10 |

Good luck!
