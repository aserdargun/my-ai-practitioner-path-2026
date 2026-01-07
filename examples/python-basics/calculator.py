#!/usr/bin/env python3
"""
Simple Calculator - Basic Python operations

This example demonstrates:
- Variables
- Arithmetic operators
- User input
- Type conversion

Run with: python calculator.py
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide a by b. Returns None if b is zero."""
    if b == 0:
        return None
    return a / b


def main():
    """Main function to run the calculator."""
    print("Simple Calculator")
    print("=" * 20)

    # Get numbers from user
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers")
        return

    # Perform calculations
    print(f"\nResults:")
    print(f"{num1} + {num2} = {add(num1, num2)}")
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
    print(f"{num1} × {num2} = {multiply(num1, num2)}")

    result = divide(num1, num2)
    if result is not None:
        print(f"{num1} ÷ {num2} = {result}")
    else:
        print(f"{num1} ÷ {num2} = Cannot divide by zero")


if __name__ == "__main__":
    main()
