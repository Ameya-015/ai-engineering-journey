import pandas as pd

reading_minutes = pd.Series([40, 0, 25, 60, 15, 90, 30], index = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])

if __name__ == "__main__":
    # The whole Series.
    print(reading_minutes)
    # Thursday’s minutes, by label.
    print(reading_minutes.loc["Thu"])
    # The last day’s minutes, by position.
    print(reading_minutes.iloc[-1])
    # Wednesday through Friday, using a label slice.
    print(reading_minutes.loc["Wed":"Fri"])
    # The first three days, using a position slice.
    print(reading_minutes.iloc[0:3])
    # Only the days with at least 30 minutes.
    print(reading_minutes[reading_minutes >= 30])
    # How many days had zero minutes.
    print((reading_minutes == 0).sum())
    # The total minutes converted to hours.
    print((reading_minutes.sum() / 60))