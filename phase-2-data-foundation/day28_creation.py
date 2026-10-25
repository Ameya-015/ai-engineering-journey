import numpy as np

even_numbers = np.arange(2, 21, 2)
grid = np.arange(1, 21).reshape(4, 5)

if __name__ == "__main__":
    # A 1D array of the even numbers from 2 to 20 inclusive, using np.arange. (Think about the stop value.)
    print(even_numbers)
    # That array reshaped into a grid with 2 rows, using -1 for the columns. Print it and its shape.
    even_grid = even_numbers.reshape(2, -1)
    print(even_grid)
    print(even_grid.shape)
    # A (3, 4) array of zeros.
    print(np.zeros((3, 4)))
    # A grid of shape (4, 5) containing the numbers 1 to 20, built with arange + reshape in one expression.
    print(grid)
    # Each row’s total from item 4, as a column vector.
    print(grid.sum(axis=1, keepdims=True))
    # A 3 × 3 array where every value is 7. (Hint: np.ones and one arithmetic operation.)
    print(np.ones((3,3)) * 7)