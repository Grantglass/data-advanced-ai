"""
Data Helper Functions

Utilities for loading, processing, and visualizing data in notebooks.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from typing import Optional, Dict, List, Union
import json


def load_sample_data(dataset_name: str, data_dir: str = "data/samples") -> pd.DataFrame:
    """
    Load a sample dataset from the data directory.

    Args:
        dataset_name: Name of the dataset (without path)
        data_dir: Directory containing sample data

    Returns:
        pandas DataFrame

    Example:
        >>> df = load_sample_data("customer_service_tickets.csv")
    """
    base_path = Path(__file__).parent.parent / data_dir
    file_path = base_path / dataset_name

    if dataset_name.endswith(".csv"):
        return pd.read_csv(file_path)
    elif dataset_name.endswith(".json"):
        with open(file_path, "r") as f:
            data = json.load(f)
            return pd.DataFrame(data)
    elif dataset_name.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {dataset_name}")


def save_results(
    data: Union[pd.DataFrame, Dict, List], filename: str, output_dir: str = "outputs"
) -> str:
    """
    Save results to file.

    Args:
        data: Data to save (DataFrame, dict, or list)
        filename: Output filename
        output_dir: Output directory

    Returns:
        str: Path to saved file
    """
    base_path = Path(__file__).parent.parent / output_dir
    base_path.mkdir(parents=True, exist_ok=True)
    file_path = base_path / filename

    if isinstance(data, pd.DataFrame):
        if filename.endswith(".csv"):
            data.to_csv(file_path, index=False)
        elif filename.endswith(".xlsx"):
            data.to_excel(file_path, index=False)
        elif filename.endswith(".json"):
            data.to_json(file_path, orient="records", indent=2)
    elif isinstance(data, (dict, list)):
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)
    else:
        raise ValueError(f"Unsupported data type: {type(data)}")

    return str(file_path)


def display_dataframe(
    df: pd.DataFrame, max_rows: int = 10, style: bool = True
) -> Union[pd.DataFrame, pd.io.formats.style.Styler]:
    """
    Display DataFrame with nice formatting.

    Args:
        df: DataFrame to display
        max_rows: Maximum number of rows to show
        style: Whether to apply styling

    Returns:
        Formatted DataFrame
    """
    display_df = df.head(max_rows)

    if style:
        return display_df.style.set_properties(
            **{
                "background-color": "#f9f9f9",
                "border-color": "black",
                "border-width": "1px",
            }
        ).set_table_styles(
            [
                {
                    "selector": "th",
                    "props": [
                        ("background-color", "#4CAF50"),
                        ("color", "white"),
                        ("font-weight", "bold"),
                    ],
                }
            ]
        )
    else:
        return display_df


def create_comparison_chart(
    data: Dict[str, List[float]],
    title: str = "Comparison",
    xlabel: str = "Category",
    ylabel: str = "Value",
    chart_type: str = "bar",
    figsize: tuple = (10, 6),
) -> plt.Figure:
    """
    Create a comparison chart from data.

    Args:
        data: Dictionary with labels as keys and values as lists
        title: Chart title
        xlabel: X-axis label
        ylabel: Y-axis label
        chart_type: Type of chart ("bar", "line", "grouped_bar")
        figsize: Figure size

    Returns:
        matplotlib Figure object

    Example:
        >>> data = {"Model A": [0.8, 0.85, 0.9], "Model B": [0.75, 0.8, 0.88]}
        >>> fig = create_comparison_chart(data, "Model Comparison")
    """
    fig, ax = plt.subplots(figsize=figsize)

    if chart_type == "bar":
        # Simple bar chart
        categories = list(data.keys())
        values = [sum(v) / len(v) if isinstance(v, list) else v for v in data.values()]
        ax.bar(categories, values, color="#4CAF50", alpha=0.7)

    elif chart_type == "grouped_bar":
        # Grouped bar chart
        df = pd.DataFrame(data)
        df.plot(kind="bar", ax=ax, rot=0)

    elif chart_type == "line":
        # Line chart
        for label, values in data.items():
            ax.plot(values, marker="o", label=label, linewidth=2)
        ax.legend()

    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    return fig


def create_evaluation_table(results: List[Dict], metrics: List[str]) -> pd.DataFrame:
    """
    Create a formatted evaluation results table.

    Args:
        results: List of result dictionaries
        metrics: List of metric names to include

    Returns:
        Formatted DataFrame
    """
    df = pd.DataFrame(results)

    # Select only specified metrics
    if metrics:
        columns = [
            col
            for col in df.columns
            if col in metrics or col in ["name", "model", "method"]
        ]
        df = df[columns]

    # Round numeric columns
    numeric_cols = df.select_dtypes(include=["float64"]).columns
    df[numeric_cols] = df[numeric_cols].round(3)

    return df


def calculate_summary_statistics(
    df: pd.DataFrame, group_by: Optional[str] = None
) -> pd.DataFrame:
    """
    Calculate summary statistics for a DataFrame.

    Args:
        df: Input DataFrame
        group_by: Optional column to group by

    Returns:
        DataFrame with summary statistics
    """
    numeric_cols = df.select_dtypes(include=["number"]).columns

    if group_by and group_by in df.columns:
        summary = df.groupby(group_by)[numeric_cols].agg(
            ["mean", "median", "std", "min", "max"]
        )
    else:
        summary = df[numeric_cols].agg(["mean", "median", "std", "min", "max"]).T

    return summary.round(2)
