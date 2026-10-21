import numpy as np

scores = np.array([[80, 90, 70],
                    [60, 75, 85],
                    [95, 88, 92],
                    [50, 65, 70]])


if __name__ == "__main__":
    print(scores.shape)
    print(scores[2])
    print(scores[:, 0])
    print(scores[3, 2])
    print(scores[:2, 1:])
    print(scores[:, 1].mean())