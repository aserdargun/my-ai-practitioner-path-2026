"""Data transformation module."""

import pandas as pd
from typing import List, Optional


def clean_missing(df: pd.DataFrame, strategy: str = "drop") -> pd.DataFrame:
    """Handle missing values."""
    if strategy == "drop":
        return df.dropna()
    elif strategy == "fill_zero":
        return df.fillna(0)
    elif strategy == "fill_mean":
        return df.fillna(df.mean(numeric_only=True))
    else:
        raise ValueError(f"Unknown strategy: {strategy}")


def normalize_columns(df: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    """Normalize specified columns to 0-1 range."""
    df = df.copy()
    for col in columns:
        if col in df.columns:
            min_val = df[col].min()
            max_val = df[col].max()
            if max_val > min_val:
                df[col] = (df[col] - min_val) / (max_val - min_val)
    return df


def add_computed_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Add computed columns. Customize as needed."""
    df = df.copy()
    # Example: add row count
    df["_row_number"] = range(len(df))
    return df


def transform_data(
    df: pd.DataFrame,
    missing_strategy: str = "drop",
    normalize_cols: Optional[List[str]] = None
) -> pd.DataFrame:
    """Apply all transformations."""
    df = clean_missing(df, missing_strategy)

    if normalize_cols:
        df = normalize_columns(df, normalize_cols)

    df = add_computed_columns(df)

    return df
