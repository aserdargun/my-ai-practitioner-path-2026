"""Data loading module."""

import pandas as pd
from pathlib import Path
from typing import Union


def load_csv(df: pd.DataFrame, filepath: Union[str, Path]) -> None:
    """Save data to CSV file."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)


def load_json(df: pd.DataFrame, filepath: Union[str, Path]) -> None:
    """Save data to JSON file."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_json(path, orient="records", indent=2)


def load_data(df: pd.DataFrame, filepath: Union[str, Path]) -> None:
    """Save data based on file extension."""
    path = Path(filepath)

    if path.suffix == ".csv":
        load_csv(df, path)
    elif path.suffix == ".json":
        load_json(df, path)
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")

    print(f"Saved {len(df)} rows to {path}")
