from datetime import datetime

from src.google_sheet import (
    connect_sheet,
    write_dataframe,
    read_symbols
)

from src.nifty250 import Nifty250
from src.market_data import MarketData
from src.indicators import Indicators


def main():

    print("Connecting to Google Sheet...")

    # Connect Google Sheet
    sheet = connect_sheet()

    # -----------------------------
    # Dashboard Update
    # -----------------------------
    dashboard = sheet.worksheet("Dashboard")

    dashboard.update(
        values=[["✅ Nifty250 Trading System Connected Successfully"]],
        range_name="A1"
    )

    dashboard.update(
        values=[[datetime.now().strftime("%d-%b-%Y %H:%M:%S")]],
        range_name="A2"
    )

    # -----------------------------
    # Download Nifty250 Master
    # -----------------------------
    nifty = Nifty250()

    master_df = nifty.download_constituents()

    write_dataframe(
        sheet,
        "Nifty250 Master",
        master_df
    )

    # -----------------------------
    # Read Symbols
    # -----------------------------
    symbols = read_symbols(sheet)

    print("Symbols Found:")
    print(symbols)

    # -----------------------------
    # Download Market Data
    # -----------------------------
    market = MarketData()

    market_df = market.fetch_market_data(symbols)

    write_dataframe(
        sheet,
        "Nifty250 Data",
        market_df
    )

    # -----------------------------
    # Calculate Indicators
    # -----------------------------
    indicator = Indicators()

    indicator_df = indicator.calculate_indicators(market_df)

    # Latest Snapshot
    latest_df = indicator.get_latest_indicators(indicator_df)

    write_dataframe(
        sheet,
        "Indicators",
        latest_df
    )

    print("Google Sheet Updated Successfully")


if __name__ == "__main__":
    main()