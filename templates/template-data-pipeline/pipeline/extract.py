"""Data extraction module."""

import pandas as pd
from pathlib import Path
from typing import Union


def extract_csv(filepath: Union[str, Path]) -> pd.DataFrame:
    """Extract data from CSV file."""
    return pd.read_csv(filepath)


def extract_json(filepath: Union[str, Path]) -> pd.DataFrame:
    """Extract data from JSON file."""
    return pd.read_json(filepath)


def extract_data(filepath: Union[str, Path]) -> pd.DataFrame:
    """Extract data based on file extension."""
    path = Path(filepath)

    if path.suffix == ".csv":
        return extract_csv(path)
    elif path.suffix == ".json":
        return extract_json(path)
    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")
