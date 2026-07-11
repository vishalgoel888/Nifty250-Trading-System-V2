import pandas as pd


class Indicators:

    def __init__(self):
        print("Indicators Module Loaded")

    def calculate_indicators(self, df):

        print("Calculating Indicators...")

        result = []

        # प्रत्येक Stock के लिए DMA Calculate करें
        for symbol, group in df.groupby("Symbol"):

            group = group.sort_values("Date").copy()

            # 50 DMA
            group["DMA50"] = (
                group["Close"]
                .rolling(window=50)
                .mean()
            )

            # 100 DMA
            group["DMA100"] = (
                group["Close"]
                .rolling(window=100)
                .mean()
            )

            # 200 DMA
            group["DMA200"] = (
                group["Close"]
                .rolling(window=200)
                .mean()
            )

            result.append(group)

        final_df = pd.concat(
            result,
            ignore_index=True
        )

        # CAR Calculate
        final_df = self.calculate_car(final_df)

        return final_df

    def calculate_car(self, df):

        print("Calculating CAR...")

        result = []

        # प्रत्येक Stock पर CAR Calculate करें
        for symbol, group in df.groupby("Symbol"):

            group = group.sort_values("Date").copy()

            # 52 Week High की Row
            high_idx = group["High"].idxmax()

            # High वाली Date से Data
            car_df = group.loc[high_idx:].copy()

            # Cumulative Average
            car_df["CAR"] = (
                car_df["Close"]
                .expanding()
                .mean()
            )

            # Original Data में CAR Column
            group["CAR"] = pd.NA

            group.loc[
                car_df.index,
                "CAR"
            ] = car_df["CAR"]

            result.append(group)

        final_df = pd.concat(
            result,
            ignore_index=True
        )

        return final_df

    def get_latest_indicators(self, df):

        print("Getting Latest Indicator Snapshot...")

        latest_df = (
            df.sort_values(["Symbol", "Date"])
              .groupby("Symbol", as_index=False)
              .tail(1)
              .reset_index(drop=True)
        )

        return latest_df