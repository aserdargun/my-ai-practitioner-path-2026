#!/usr/bin/env python3
"""
Pandas Introduction - Basic data analysis

This example demonstrates:
- Creating DataFrames
- Basic operations
- Data exploration
- Simple analysis

Run with: python pandas_intro.py
"""

import pandas as pd


def main():
    # Create a simple DataFrame
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "age": [25, 30, 35, 28, 32],
        "city": ["NYC", "LA", "Chicago", "NYC", "LA"],
        "salary": [50000, 60000, 75000, 55000, 65000]
    }

    df = pd.DataFrame(data)

    # Basic exploration
    print("Our DataFrame:")
    print(df)
    print()

    print("DataFrame info:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    print()

    print("Statistical summary:")
    print(df.describe())
    print()

    # Simple analysis
    print("Analysis:")
    print(f"Average age: {df['age'].mean():.1f}")
    print(f"Average salary: ${df['salary'].mean():,.0f}")
    print()

    # Filtering
    print("People in NYC:")
    nyc_people = df[df["city"] == "NYC"]
    print(nyc_people)
    print()

    # Grouping
    print("Average salary by city:")
    by_city = df.groupby("city")["salary"].mean()
    print(by_city)


if __name__ == "__main__":
    main()
