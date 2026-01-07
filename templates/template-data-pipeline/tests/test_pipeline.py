"""Tests for data pipeline."""

import pytest
import pandas as pd
from pipeline.extract import extract_data
from pipeline.transform import transform_data, clean_missing, normalize_columns


@pytest.fixture
def sample_df():
    """Create sample DataFrame for testing."""
    return pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "score": [80.0, 90.0, 85.0]
    })


@pytest.fixture
def df_with_missing():
    """Create DataFrame with missing values."""
    return pd.DataFrame({
        "name": ["Alice", None, "Charlie"],
        "age": [25, 30, None],
        "score": [80.0, None, 85.0]
    })


def test_clean_missing_drop(df_with_missing):
    """Test dropping missing values."""
    result = clean_missing(df_with_missing, "drop")
    assert len(result) == 1
    assert result.iloc[0]["name"] == "Alice"


def test_clean_missing_fill_zero(df_with_missing):
    """Test filling missing with zeros."""
    result = clean_missing(df_with_missing, "fill_zero")
    assert len(result) == 3
    assert result["score"].iloc[1] == 0


def test_normalize_columns(sample_df):
    """Test column normalization."""
    result = normalize_columns(sample_df, ["age"])
    assert result["age"].min() == 0.0
    assert result["age"].max() == 1.0


def test_transform_data(sample_df):
    """Test full transformation."""
    result = transform_data(sample_df)
    assert "_row_number" in result.columns
    assert len(result) == 3
