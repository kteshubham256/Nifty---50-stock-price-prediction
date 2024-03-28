# Install yfinance library for fetching stock data
# Import yfinance and pandas libraries for fetching and manipulating stock data
pip instal yfinance --q
import yfinance as yf
import pandas as pd

# Nifty 50 stocks
stocks = pd.read_csv('Nifty_stocks.csv')
stocks.head()

stocks.columns = stocks.columns.str.strip()
stocks.head()

nifty_stocks = pd.Series(stocks['SYMBOL'][1:])
nifty_stocks

start_date = '2020-01-01'
end_date = '2024-01-01'

nifty_data = {}
for stock in nifty_stocks:
    data = yf.download(f'{stock}.NS', start=start_date, end=end_date)
    nifty_data[stock] = data

nifty_data['RELIANCE']

# We got data for all 50 stocks from 2020 to 2023 = last 4 years

nifty_data['ONGC']

