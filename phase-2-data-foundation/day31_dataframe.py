import pandas as pd

plants = pd.DataFrame({"plant": ["Fern", "Cactus", "Basil", "Monstera", "Aloe"],
                               "height_cm" : [30, 15, 25, 80, 20],
                               "days_since_watered" : [2, 14, 1, 5, 9],})

if __name__ == "__main__":
    # The whole table.
    print(plants)
    # Its shape.
    print(plants.shape)
    # The height_cm column, as a Series.
    print(plants["height_cm"])
    # The plant and days_since_watered columns, as a DataFrame.
    print(plants[["plant", "days_since_watered"]])
    # Basil’s height, using .loc (with its row label and column name).
    print(plants.loc[2, "height_cm"])
    # The same value, using .iloc (positions).
    print(plants.iloc[2,1])
    # The plant names for rows 1 through 3 inclusive, using a label slice.
    print(plants.loc[1:3, "plant"])
    # The average height.
    print(plants["height_cm"].mean())
    # The column dtypes.
    print(plants.dtypes)