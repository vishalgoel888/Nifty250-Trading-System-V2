import pandas as pd


class Nifty250:

    def __init__(self):
        print("Nifty250 Module Loaded")

    def download_constituents(self):

        print("Downloading Nifty250 Constituents...")

        # अभी Dummy Data
        # अगले Step में यही Official Download होगा
        df = self._get_dummy_data()

        # Master Sheet Format
        df = self._prepare_master(df)

        return df

    def _get_dummy_data(self):

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

        return df

    def _download_official_data(self):

        print("Downloading Official Nifty250 Data...")

        # अगले Step में Official Download Code आएगा
        pass

    def _prepare_master(self, df):

        df["Industry"] = ""
        df["Series"] = "EQ"
        df["ISIN"] = ""
        df["Active"] = "YES"

        return df