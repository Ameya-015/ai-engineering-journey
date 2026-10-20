import numpy as np


if __name__ == "__main__":
    prices = np.array([20, 40, 60, 80, 100])

    # Price after applying 10% discount to all prices
    print(prices * 0.90)
    # Calculate mean of prices array
    print(prices.mean())
    # Get index of the product having maximum price
    print(prices.argmax())
    # Every element's difference from the mean/avg
    print(prices - prices.mean())