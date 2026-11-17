# Predicting Stock Outperformance from Public Financial Statement Data

DS 4021 Final Project, Fall 2026

**Group:** Audrey Stelle, Claire Newsom, Jonathan Lee

## Research question

Using the financial indicators that U.S. public companies report in their annual 10-K filings, can machine learning models predict which stocks will outperform the median stock over the following year, and which indicators matter most for these predictions?

## Data

We use the [200+ Financial Indicators of US Stocks (2014-2018)](https://www.kaggle.com/datasets/cnic92/200-financial-indicators-of-us-stocks-20142018) dataset from Kaggle by Nicolas Carbone. There is one file per year. Each row is a U.S. listed company with 221 financial indicators from its 10-K filing for that year, its sector, its stock price change over the following year (`PRICE VAR [%]`) and `Class` (1 if that price change was zero or positive, 0 if it was negative).

| Folder | Years | Rows | Use |
|---|---|---|---|
| `Data/training_set/` | 2014 to 2017 | 17,685 | Everything: exploring, cleaning, cross-validation and tuning |
| `Data/reporting_set/` | 2018 | 4,392 (19.9%) | **Do not open until the final phase** |

The reporting set is the most recent year instead of a random 20%. Stocks in the same year move together with the market, so a random split would let the models learn from the same year they are tested on. Holding out the last year means the final test is on a year the models have never seen, like in real investing.

The CSV files are exact copies of the original Kaggle files. See `Data/README.md` for the columns and a few things to know about the data.

## Loading the data

```python
from load_data import load_training_set

train = load_training_set()  # 17,685 rows, the four training years stacked
```

`load_training_set()` adds a `Year` column, renames each year's price change column to `Next Year Price Var [%]`, and adds `Beat Median` (1 if the stock's next-year price change was above the median stock that year). `Beat Median` is the target for our research question.
