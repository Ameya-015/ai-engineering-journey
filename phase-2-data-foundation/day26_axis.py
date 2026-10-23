import numpy as np

daily_steps = np.array([[ 8000, 12000,  6000, 10500],
                    [11000,  9000, 13000, 14000],
                    [ 4000,  7000,  5000,  6500]])

if __name__ == "__main__":
    print(daily_steps.mean(axis = 1))
    print(daily_steps.sum(axis = 0))
    print(daily_steps.max(axis = 1))
    print((daily_steps >= 10000).sum(axis = 1))
    print((daily_steps >= 10000).sum())
    