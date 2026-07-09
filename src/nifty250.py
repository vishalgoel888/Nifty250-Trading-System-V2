import pandas as pd


class Nifty250:

    def __init__(self):
        print("Nifty250 Module Loaded")

    def download_constituents(self):

        print("Downloading Nifty250 Constituents...")

        data = [
            ["RELIANCE", "Reliance Industries Ltd"],
            ["TCS", "Tata Consultancy Services Ltd"],
            ["HDFCBANK", "HDFC Bank Ltd"],
            ["INFY", "Infosys Ltd"],
            ["ICICIBANK", "ICICI Bank Ltd"]
        ]

        df = pd.DataFrame(
            data,
            columns=["Symbol", "Company"]
        )

        print(df)

        return df