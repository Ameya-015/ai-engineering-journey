import numpy as np

weekly_hours = np.array([[ 5, 2, 8],
                        [ 3, 6, 1],
                        [ 7, 4, 4],
                        [ 1, 8, 3]])

if __name__ == "__main__":
    # Every value converted to minutes.
    print(weekly_hours * 60)
    # Each hobby’s average hours (one per hobby).
    print(weekly_hours.mean(axis=0))
    # The array centered per hobby: each value minus its hobby’s average.
    print(weekly_hours - weekly_hours.mean(axis=0))
    # Each person’s total hours, as a column vector of shape (4, 1). (Hint: Day 24 showed you how slicing keeps dimensions. NumPy also has a keepdims=True argument on aggregations that does this. Try it.)
    print(weekly_hours.sum(axis=1, keepdims=True))
    # Each value as a fraction of that person’s total (each row should sum to 1). Use item 4’s result.
    total_hours = weekly_hours.sum(axis=1,keepdims=True)
    print(weekly_hours / total_hours)
    # The shape of the item-4 result, as a check.
    print(total_hours.shape)