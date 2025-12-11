# Medicine Stock-Out Early Warning System

This project predicts medicine shortages using data on stock levels, daily usage, and delivery dates.
It generates warnings for medicines that are at risk of running out before their next delivery.

## Features
- Loads medicine stock data from a CSV file
- Estimates days until each medicine runs out
- Compares with next delivery date and safety thresholds
- Prints a clear, text-based report

## How it works
1. Load data from `sample_data.csv`.
2. Calculate how many days each medicine will last.
3. Compare with the next delivery date.
4. Print warnings and status messages.

## How to run
Run the Python script with this command:python3 stock_alert.py
## Files
- `stock_alert.py` — main program
- `sample_data.csv` — example data
- `README.md` — this documentation
