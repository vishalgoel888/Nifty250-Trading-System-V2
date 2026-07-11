import yfinance as yf
import pandas as pd


class MarketData:

    def __init__(self):
        print("Market Data Module Loaded")

    def fetch_market_data(self, symbols):

        print(f"Downloading data for {len(symbols)} stocks...")

        raw_df = yf.download(
            tickers=symbols,
            period="1y",
            interval="1d",
            auto_adjust=True,
            group_by="ticker",
            progress=True
        )

        clean_df = self.normalize_market_data(raw_df)

        print(clean_df.head())

        return clean_df

    def normalize_market_data(self, raw_df):

        print("Normalizing Market Data...")

        all_data = []

        symbols = raw_df.columns.levels[0]

        for symbol in symbols:

            df = raw_df[symbol].copy()

            df.reset_index(inplace=True)

            df.insert(0, "Symbol", symbol.replace(".NS", ""))

            all_data.append(df)

        final_df = pd.concat(
            all_data,
            ignore_index=True
        )

        return final_df

    def update_data_sheet(self):
        print("Updating Nifty250 Data Sheet...")