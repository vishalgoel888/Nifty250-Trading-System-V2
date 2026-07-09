from datetime import datetime
from src.google_sheet import connect_sheet, write_dataframe
from src.nifty250 import Nifty250
from src.market_data import MarketData


def main():

    print("Connecting to Google Sheet...")

    sheet = connect_sheet()

    dashboard = sheet.worksheet("Dashboard")

    dashboard.update(
        values=[["✅ Nifty250 Trading System Connected Successfully"]],
        range_name="A1"
    )

    dashboard.update(
        values=[[datetime.now().strftime("%d-%b-%Y %H:%M:%S")]],
        range_name="A2"
    )

    nifty = Nifty250()

    df = nifty.download_constituents()

    write_dataframe(sheet, "Nifty250 Master", df)

    market = MarketData()

    market.fetch_market_data()

    print("Google Sheet Updated Successfully")


if __name__ == "__main__":
    main()