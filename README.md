# Earnings Monitor

An interactive Earnings Monitor web application.

## Project Structure

## How to Run

### Step 1 — Install dependencies
```bash
pip install requests pandas
```

### Step 2 — Fetch live data
```bash
python fetch_earnings.py
```
This generates `earnings_data.json` with the latest earnings data for all 50 tickers.

### Step 3 — Open the dashboard
Open `src/index.html` using Live Server in VS Code, or any local web server.
Do not open directly as a `file://` URL — the data will not load.

## Data Sources
- Earnings data: Yahoo Finance (via direct API calls)

## GitHub Repository
https://github.com/athomas99-99/earnings-monitor