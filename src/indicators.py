import pandas as pd


class Indicators:

    def __init__(self):
        print("Indicators Module Loaded")

    def calculate_indicators(self, df):

        print("Calculating Indicators...")

        result = []

        # Calculate DMA for each stock
        for symbol, group in df.groupby("Symbol"):

            group = group.sort_values("Date").copy()

            # DMA 50
            group["DMA50"] = (
                group["Close"]
                .rolling(window=50)
                .mean()
            )

            # DMA 100
            group["DMA100"] = (
                group["Close"]
                .rolling(window=100)
                .mean()
            )

            # DMA 200
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

        # Calculate CAR
        final_df = self.calculate_car(final_df)

        # Check CAR Signal
        final_df = self.check_car_signal(final_df)

        return final_df

    def calculate_car(self, df):

        print("Calculating CAR...")

        result = []

        for symbol, group in df.groupby("Symbol"):

            group = group.sort_values("Date").copy()

            # 52 Week High Row
            high_idx = group["High"].idxmax()

            # Data from High Date onwards
            car_df = group.loc[high_idx:].copy()

            # Cumulative Average
            car_df["CAR"] = (
                car_df["Close"]
                .expanding()
                .mean()
            )

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

    def check_car_signal(self, df):

        print("Checking CAR Signal...")

        result = []

        for symbol, group in df.groupby("Symbol"):

            group = group.sort_values("Date").copy()

            signal = "NEGATIVE"

            car_values = group["CAR"].dropna()

            if len(car_values) >= 10:

                last10 = car_values.tail(10).tolist()

                increasing = all(
                    last10[i] > last10[i - 1]
                    for i in range(1, len(last10))
                )

                if increasing:
                    signal = "POSITIVE"

            group["CAR_SIGNAL"] = signal

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