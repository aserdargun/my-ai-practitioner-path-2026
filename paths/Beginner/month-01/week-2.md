# Week 2: Data Types & Control Flow

**Focus**: Python data types and control structures

---

## Objectives

- [ ] Master Python data types (strings, numbers, lists, dicts)
- [ ] Use conditional statements (if/elif/else)
- [ ] Write loops (for, while)
- [ ] Understand list comprehensions
- [ ] Practice with real-world examples

---

## Tasks

### Day 1-2: Data Types

1. **Strings**
   ```python
   text = "Hello, Python!"
   print(text.upper())        # HELLO, PYTHON!
   print(text.split(","))     # ['Hello', ' Python!']
   print(len(text))           # 14
   print(text[0:5])           # Hello
   ```

2. **Numbers**
   ```python
   integer = 42
   floating = 3.14
   result = integer + floating  # 45.14

   # Useful operations
   print(10 // 3)   # 3 (integer division)
   print(10 % 3)    # 1 (remainder)
   print(2 ** 10)   # 1024 (power)
   ```

3. **Lists**
   ```python
   fruits = ["apple", "banana", "cherry"]
   fruits.append("date")
   fruits.remove("banana")
   print(fruits[0])      # apple
   print(fruits[-1])     # date
   print(len(fruits))    # 3
   ```

4. **Dictionaries**
   ```python
   person = {
       "name": "Alice",
       "age": 30,
       "city": "NYC"
   }
   print(person["name"])      # Alice
   person["email"] = "a@b.com"
   print(person.keys())       # dict_keys(['name', 'age', 'city', 'email'])
   ```

### Day 3-4: Control Flow

1. **Conditionals**
   ```python
   age = 25

   if age < 18:
       print("Minor")
   elif age < 65:
       print("Adult")
   else:
       print("Senior")
   ```

2. **For Loops**
   ```python
   # Loop through list
   for fruit in ["apple", "banana", "cherry"]:
       print(fruit)

   # Loop with range
   for i in range(5):
       print(i)  # 0, 1, 2, 3, 4

   # Loop through dict
   for key, value in person.items():
       print(f"{key}: {value}")
   ```

3. **While Loops**
   ```python
   count = 0
   while count < 5:
       print(count)
       count += 1
   ```

### Day 5: List Comprehensions

```python
# Traditional loop
squares = []
for x in range(10):
    squares.append(x ** 2)

# List comprehension (same result)
squares = [x ** 2 for x in range(10)]

# With condition
evens = [x for x in range(20) if x % 2 == 0]

# Dictionary comprehension
square_dict = {x: x ** 2 for x in range(5)}
```

---

## Exercises

### Exercise 1: Grade Calculator

```python
# Given a score, print the letter grade
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
```

### Exercise 2: Shopping List

```python
# Manage a shopping list
shopping = []

# Add items
shopping.append("milk")
shopping.append("bread")
shopping.append("eggs")

# Print all items
for item in shopping:
    print(f"- {item}")

# Check if item exists
if "milk" in shopping:
    print("Don't forget the milk!")
```

### Exercise 3: Word Counter

```python
# Count words in a sentence
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
```

---

## Checklist

- [ ] Practiced string operations
- [ ] Worked with lists and dictionaries
- [ ] Wrote conditional statements
- [ ] Created for and while loops
- [ ] Used list comprehensions
- [ ] Completed all exercises
- [ ] Made regular commits
- [ ] Wrote week 2 journal entry

---

## Reflection Prompt

*Which data structure (list vs dictionary) do you find more intuitive? When would you use each?*

---

## Next

Proceed to [Week 3](week-3.md) for functions and modules.
