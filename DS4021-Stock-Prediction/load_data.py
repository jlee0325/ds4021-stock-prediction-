"""Load the project data.

Use load_training_set() for everything until the final phase of the project.
load_reporting_set() is only for the final phase.
"""
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent / "Data"


def _load_year(path, year):
    df = pd.read_csv(path).copy()
    df = df.rename(columns={df.columns[0]: "Ticker", f"{year + 1} PRICE VAR [%]": "Next Year Price Var [%]"})
    df.insert(1, "Year", year)
    next_year = df["Next Year Price Var [%]"]
    df["Beat Median"] = (next_year > next_year.median()).astype(int)
    return df


def load_training_set():
    """2014 to 2017 stacked into one table (17,685 rows)."""
    files = sorted((DATA / "training_set").glob("*_Financial_Data.csv"))
    return pd.concat([_load_year(f, int(f.name[:4])) for f in files], ignore_index=True)


def load_reporting_set():
    """2018 (4,392 rows). Only use this in the final phase of the project."""
    return _load_year(DATA / "reporting_set" / "2018_Financial_Data.csv", 2018)


if __name__ == "__main__":
    train = load_training_set()
    print(train.shape)
    print(train.groupby("Year")[["Class", "Beat Median"]].mean().round(3))
