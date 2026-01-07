"""Pipeline orchestration."""

import argparse
from pathlib import Path
from pipeline.extract import extract_data
from pipeline.transform import transform_data
from pipeline.load import load_data


def run_pipeline(
    input_path: str,
    output_path: str,
    missing_strategy: str = "drop"
) -> None:
    """Run the complete ETL pipeline."""
    print(f"Starting pipeline...")
    print(f"Input: {input_path}")
    print(f"Output: {output_path}")

    # Extract
    print("Extracting data...")
    df = extract_data(input_path)
    print(f"Extracted {len(df)} rows")

    # Transform
    print("Transforming data...")
    df = transform_data(df, missing_strategy=missing_strategy)
    print(f"Transformed to {len(df)} rows")

    # Load
    print("Loading data...")
    load_data(df, output_path)

    print("Pipeline complete!")


def main():
    parser = argparse.ArgumentParser(description="Run data pipeline")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument(
        "--missing-strategy",
        default="drop",
        choices=["drop", "fill_zero", "fill_mean"],
        help="Strategy for handling missing values"
    )

    args = parser.parse_args()
    run_pipeline(args.input, args.output, args.missing_strategy)


if __name__ == "__main__":
    main()
