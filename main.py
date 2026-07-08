from datetime import datetime
from src.google_sheet import connect_sheet


def main():

    print("Connecting to Google Sheet...")

    sheet = connect_sheet()

    dashboard = sheet.worksheet("Dashboard")

    dashboard.update(
        "A1",
        [["✅ Nifty250 Trading System Connected Successfully"]]
    )

    dashboard.update(
        "A2",
        [[datetime.now().strftime("%d-%b-%Y %H:%M:%S")]]
    )

    print("Google Sheet Updated Successfully")


if __name__ == "__main__":
    main()