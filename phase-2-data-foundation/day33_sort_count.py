import pandas as pd

workouts = pd.DataFrame({"activity": ["run", "yoga", "cycle", "run", "swim", "yoga", "run"],
                         "minutes": [30, 45, 60, 25, 40, 30, 35],
                         "calories": [300, 150, 450, 250, 350, 100, 350],
                         "day": ["Mon", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]})

if __name__ == "__main__":
    # The whole table sorted by calories, highest first.
    print(workouts.sort_values("calories", ascending=False))
    # The top 3 workouts by minutes (whole rows).
    print(workouts.sort_values("minutes", ascending=False).head(3))
    # The table sorted by activity A→Z, with ties broken by minutes longest first.
    print(workouts.sort_values(["activity", "minutes"], ascending=[True, False]))
    # How many times each activity appears.
    print(workouts["activity"].value_counts())
    # The most common activity, as a single value.
    print(workouts["activity"].value_counts().index[0])
    # The fraction of workouts that were yoga, as a single number.
    print(workouts["activity"].value_counts(normalize=True)["yoga"])
    # How many workouts fall on each day, ordered Mon to Sat as they appear in the label order (use sort_index(), 
    # then see what order you actually get, and add a comment explaining it).
    print(workouts["day"].value_counts().sort_index())
    # Above print will print the day in alphabetical order