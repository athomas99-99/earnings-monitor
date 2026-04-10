# Earnings Monitor

An interactive Earnings Monitor web application.

## Project Structure

## How to Run

### Step 1 — Install dependencies
```bash
pip install requests pandas yfinance
```

### Step 2 — Fetch live data
```bash
python fetch_earnings.py
```
This generates `earnings_data.json` with the latest earnings data for all 50 tickers.

### Step 3 — Open the dashboard
Open `src/index.html` using one of these methods:

**Option A: VS Code Live Server**
1. Open VS Code and load the earnings-monitor folder
2. Install the Live Server extension in VS Code
3. Right-click `src/index.html` → Open with Live Server
4. The dashboard will open automatically in your browser

**Option B: Python local host**
Run the following script in the terminal :
```bash
cd src
python -m http.server 8000
```
Then open `http://localhost:8000` in your browser.

Do NOT open index.html by double-clicking it

## Data Sources
- Earnings data: Yahoo Finance (via direct API calls)

## GitHub Repository
https://github.com/athomas99-99/earnings-monitor