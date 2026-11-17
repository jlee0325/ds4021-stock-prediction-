# Data

- `training_set/` has the 2014, 2015, 2016 and 2017 files (17,685 company-years). Use these for everything until the final phase.
- `reporting_set/` has the 2018 file (4,392 companies, 19.9% of the data). **Do not open, explore or use it until the final phase of the project.**

All five files are exact copies of the files in the original Kaggle download: https://www.kaggle.com/datasets/cnic92/200-financial-indicators-of-us-stocks-20142018

## Columns

- First column (no name): the stock ticker
- 221 financial indicators from the company's 10-K for that year (the same 221 columns every year)
- `Sector`: one of 11 sectors
- `YYYY PRICE VAR [%]`: the stock's price change over the next year, from its first trading day to its last trading day (for example, `2015 PRICE VAR [%]` in the 2014 file)
- `Class`: 1 if that price change was zero or positive, 0 if it was negative

## Things to know

- 15.4% of the indicator values are missing, and every row has at least one missing value, so we will need to handle missing data.
- A few price changes are huge (the largest is over 2,000,000%), and these are most likely data errors.
- The share of stocks that went up swings from 27.6% to 70.2% depending on the year because of how the overall market did. This is why our target is beating the median stock of the same year (`Beat Median` in `load_data.py`) instead of `Class`.
- Companies file their 10-K a few weeks to a few months after their fiscal year ends, but the price change starts on the first trading day of the next year. So some indicators were not public yet when the price change starts.
