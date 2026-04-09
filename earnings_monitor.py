# %%
import yfinance as yf
import pandas as pd
import json
from datetime import date, datetime
import requests
import math

# %%
df = pd.read_csv("Sample_Stocks.csv")
tickers = df["Ticker"].tolist()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    'Cookie' : 'tbla_id=84f18184-6486-4949-bd0a-7e69c47d1e92-tuctc2317d8; Y=v=1&n=5011cf0dumsvv&l=v05e5lwk9hjat6xhs18wsghpo1ufkhjd6xt7l21a/o&p=034vvvv00000000&r=1g1&intl=us; _ebd=bid-8bhh8ipiij35v&d=e4f6fbc268dff699c11a9385d9e46673&s=bidhashk-EhWPKBbF; axids=gam=y-h5I9F1pG2uIlSdOGekrde49c2y5n3_oso2ae5wQ8V_ENgBiTCw---A&dv360=eS1CTWRmUjdkRTJ1R0VsVHNGMF96QzFtVExKcUlEN0pFLkcwaWx2UFdEZDRZQndVYUVYYVRNT0NNdXlBUDFldzBienluWH5B&ydsp=y-TC.WS9NE2uIs9OIyD1gCpj2ApPouGVPG7wY5d6.mJZFvLgw9.Bx1AxCPtMmUsnS0MKuz~A&tbla=y-97cyGKVG2uJqpD78rpS2RranUXpjigwFKaH5rg0Rk07lKtoK6g---A; OTH=v=2&s=0&d=eyJraWQiOiIwIiwiYWxnIjoiUlMyNTYifQ.eyJjdSI6eyJndWlkIjoiRTdLVExERk1KNjZSMjI2Q0JLRUdJSUwyU1UiLCJwZXJzaXN0ZW50Ijp0cnVlLCJzaWQiOiJWZVNscU1rTVM5dmIifX0.tj8azYsssMMVO64yUPHq3E2SxPtm7wD1MW02S2f3yyhklny2ZHui2MrvxnbJtzrlf9MyOMqk2bAcpHqktp6Hx9kEFLwUY7ijuTK0dzeofzOPuYnHbLLlWFk5ih_karkJ4GBR_Rx9xfqm8t0X2VFq2laIqxVItFKbmrBk8-x3LcI; T=af=JnRzPTE3NjU5Nzc3NDQmcHM9WXl6bDl4aHZaMkl4cXlBMDBUSDNkUS0t&d=bnMBeWFob28BZwFFN0tUTERGTUo2NlIyMjZDQktFR0lJTDJTVQFhYwFBTXYwd0FXYgFhbAFqdW5rNjQ5OQFzYwFkZXNrdG9wX3dlYgFmcwEuVnhvR1I1cFFxUngBenoBUTZxUXBCLjZFAWEBUUFFAWxhdAFaNHFRcEIBbnUBMAF0ZgFCQUE-&kt=EAAXNJFDGdUVlnxIQHGEnPSYw--~I&ku=FAAg2w0Qnl3Ps6VzCvfE6162coRk5clLVHffppTbTJoXYe8xN9xNjmG4O0xmQCpGDIps.gGqOHqFuH6zxoDbV9rY3KmoY9lU8y3yj8KPpIcZjMqT9OHWuYGzxA1J7NAzCfoeTxRgF.KxDYpwXaI8IsLzyJFbIZ6RZv.HI2L9uulpG8-~E; OTHD=g=828012EF97F672738E41D063728E95AD9CF20C402AFBB20E4AB528288BEC43F6&s=8CDC6B17DD63F8F9D78ABF7DA8F634A9E77D7D2DDBDCAE986B63EB3D4D61D99D&b=bid-8bhh8ipiij35v&j=us&bd=8f864f6ebe58073ea89b7ad81080ebfb&gk=x1a9z-qJCjBBcc&sk=x1a9z-qJCjBBcc&bk=x1a9z-qJCjBBcc&iv=1FA17492033CE963442D9F5046AF79B7&v=1&u=0; ySID=v=1&d=OxjL.5jJ1Q--; GUC=AQEBCAFp1qxp_kIf-QSW&s=AQAAADs-2Hg4&g=adVoRg; A1=d=AQABBL-MKWUCEBtmfuME4Xn0gwIOkJYoxoUFEgEBCAGs1mn-adxF0iMA_eMDAAcIv4wpZZYoxoUID_Iai8UiVGkJReOxfM2IWAkBBwoB1w&S=AQAAAsmVZx4hpjnT44PEesCqiWo; A3=d=AQABBL-MKWUCEBtmfuME4Xn0gwIOkJYoxoUFEgEBCAGs1mn-adxF0iMA_eMDAAcIv4wpZZYoxoUID_Iai8UiVGkJReOxfM2IWAkBBwoB1w&S=AQAAAsmVZx4hpjnT44PEesCqiWo; A1S=d=AQABBL-MKWUCEBtmfuME4Xn0gwIOkJYoxoUFEgEBCAGs1mn-adxF0iMA_eMDAAcIv4wpZZYoxoUID_Iai8UiVGkJReOxfM2IWAkBBwoB1w&S=AQAAAsmVZx4hpjnT44PEesCqiWo; cmp=t=1775593534&j=0&u=1YNN; gpp=DBABLA~BVRqAAAAAmA.QA; gpp_sid=7; _ga=GA1.1.176471743.1775593536; fes-ds-session=pv%3D4; PRF=t%3DAAPL%26dock-collapsed%3Dtrue; _ga_YD9K1W9DLN=GS2.1.s1775593535$o1$g1$t1775595595$j56$l0$h0'
}

crumb = "znZTCYGPJke"

for i in tickers:
    url = f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{i}?modules=calendarEvents%2Cearnings%2CearningsTrend&crumb={crumb}"
    response = requests.get(url, headers=headers)
    response_json = response.json()
    response.status_code
    print(response_json)

# %%
def extract_fields(response_json, ticker, company, sector, headers, crumb):
    try:
        result = response_json["quoteSummary"]["result"][0]
        
        # Industry
        try:
            industry = result["assetProfile"]["industry"]
        except:
            industry = None

        # Market Cap
        try:
            market_cap = result["summaryDetail"]["marketCap"]["raw"]
        except:
            market_cap = None
        
        # Earnings Date and time
        try:
            raw_date = result["calendarEvents"]["earnings"]["earningsDate"][0]["raw"]
            next_eps_date = datetime.fromtimestamp(raw_date).strftime("%Y-%m-%d")
            earnings_dt = datetime.fromtimestamp(raw_date)
            earnings_hour = earnings_dt.hour
            
            # Before 12pm = BMO, after 4pm = AMC
            if earnings_hour < 12:
                earnings_time = "BMO"
            elif earnings_hour >= 16:
                earnings_time = "AMC"
            else:
                earnings_time = "During Market"
                
            # Full formatted datetime
            next_eps_datetime = earnings_dt.strftime("%Y-%m-%d %I:%M %p")
        except:
            earnings_time = None
            next_eps_date = None
            next_eps_datetime = None

        # Earnings Trend fields
        try:
            trend = result["earningsTrend"]["trend"]
            current_quarter = next(t for t in trend if t["period"] == "0q")
            
            last_eps_date        = current_quarter["endDate"]
            revenue_estimate     = current_quarter["revenueEstimate"]["avg"]["raw"]
            year_ago_sales       = current_quarter["revenueEstimate"]["yearAgoRevenue"]["raw"]
            sales_growth_rate    = current_quarter["growth"]["raw"]
        except:
            last_eps_date = revenue_estimate = year_ago_sales = sales_growth_rate = None

        # Days since/till EPS
        try:
            today = date.today()
            
            next_date = datetime.strptime(next_eps_date, "%Y-%m-%d").date()
            last_date = datetime.strptime(last_eps_date, "%Y-%m-%d").date()
            
            days_till_next_eps  = (next_date - today).days
            days_since_last_eps = (today - last_date).days
        except:
            days_till_next_eps = days_since_last_eps = None

        # Current EPS estimate
        try:
            current_estimate = result["earnings"]["earningsChart"]["currentQuarterEstimate"]["raw"]
        except:
            current_estimate = None

        # Last reported quarter (actual vs estimate)
        try:
            quarterly = result["earnings"]["earningsChart"]["quarterly"]
            last_quarter  = quarterly[-1]
            last_actual   = last_quarter["actual"]["raw"]
            last_estimate = last_quarter["estimate"]["raw"]
            hit_miss_dollar = round(last_actual - last_estimate, 4)
            hit_miss_pct    = round((hit_miss_dollar / abs(last_estimate)) * 100, 2) if last_estimate != 0 else None
        except:
            last_actual = last_estimate = hit_miss_dollar = hit_miss_pct = None

        # Last EPS Growth Rate
        try:
            # Growth rate = (last_actual - year_ago_eps) / abs(year_ago_eps)
            year_ago_eps = result["earningsTrend"]["trend"][0]["earningsEstimate"]["yearAgoEps"]["raw"]
            last_eps_growth = round((last_actual - year_ago_eps) / abs(year_ago_eps) * 100, 2) if year_ago_eps != 0 else None
        except:
            last_eps_growth = None
        
        # Daily Return
        try:
            price_url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?interval=1d&range=5d&crumb={crumb}"
            price_response = requests.get(price_url, headers=headers)
            prices = price_response.json()["chart"]["result"][0]["indicators"]["quote"][0]["close"]
            prices = [p for p in prices if p is not None]
            daily_return = round((prices[-1] - prices[-2]) / prices[-2] * 100, 2)
        except:
            daily_return = None

        return {
            "ticker": ticker,
            "company": company,
            "sector": sector,
            "industry": industry,
            "market_cap": market_cap,
            "next_eps_datetime": next_eps_datetime,
            "days_till_next_eps": days_till_next_eps,
            "days_since_last_eps": days_since_last_eps,
            "current_estimate": current_estimate,
            "revenue_estimate": revenue_estimate,
            "year_ago_sales": year_ago_sales,
            "sales_growth_rate": round(sales_growth_rate * 100, 2) if sales_growth_rate else None,
            "last_eps_date": last_eps_date,
            "last_actual": last_actual,
            "last_estimate": last_estimate,
            "last_eps_growth": last_eps_growth,
            "hit_miss_dollar": hit_miss_dollar,
            "hit_miss_pct": hit_miss_pct,
            "daily_return": daily_return,
        }

    except Exception as e:
        print(f"  Error parsing {ticker}: {e}")
        return {"ticker": ticker, "company": company, "sector": sector}


# Main loop
results = []

for _, row in df.iterrows():
    sym = row["Ticker"].replace(".", "-")
    url = url = f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{sym}?modules=calendarEvents%2Cearnings%2CearningsTrend%2CassetProfile%2CdefaultKeyStatistics%2CfinancialData%2CsummaryDetail&crumb={crumb}"

    response = requests.get(url, headers=headers)
    data = response.json()
    
    record = extract_fields(data, sym, row["Company"], row["Sector"], headers, crumb)
    results.append(record)
    print(f"{sym}")

# Preview as a table
pd.DataFrame(results)

# %%
data = pd.DataFrame(results).to_dict(orient="records")

# Replace NaN values recursively
def clean_nans(obj):
    if isinstance(obj, dict):
        return {k: clean_nans(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [clean_nans(v) for v in obj]
    elif isinstance(obj, float) and math.isnan(obj):
        return None
    return obj

cleaned_data = clean_nans(data)

with open("earnings_data.json", "w") as f:
    json.dump(cleaned_data, f, indent=2)

print("Saved")


