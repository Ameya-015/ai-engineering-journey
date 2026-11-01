import pandas as pd

books = pd.DataFrame({"book": ["Dune", "Emma", "Ulysses", "Beloved", "Hamlet"],
                        "pages": [412, 474, 730, 324, 160],
                        "pages_read": [412, 120, 50, 324, 80],
                        "rating": [5, 3, 2, 4, 4]})

if __name__ == "__main__":
    # Add a column pages_left: pages minus pages read.
    books["pages_left"] = books["pages"] - books["pages_read"]
    # Add a column progress: the fraction read, from 0 to 1.
    books["progress"] = books["pages_read"] / books["pages"]
    # Add a boolean column finished: True when the book is fully read.
    books["finished"] = books["pages"] == books["pages_read"]
    # Print the whole table.
    print(books)
    # Print only the unfinished books (use your finished column with ~).
    print(books[~books["finished"]])
    # Print the names of books rated at least 4 that are not finished, using .loc with a mask and a column name.
    print(books.loc[(books["rating"] >= 4) & ~(books["finished"]), "book"])
    # Print how many books are finished.
    print(books["finished"].sum())
    # Print the total pages left across all books.
    print(books["pages_left"].sum())