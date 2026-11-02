import pandas as pd

tasks = [("write report", 3), ("email", 1), ("code review", 2), ("plan sprint", 5)]

movies = pd.DataFrame({"title": ["Arrival", "Up", "Dune", "Coco"],
                       "minutes": [116, 96, 155, 105],
                       "year": [2016, 2009, 2021, 2017]})

def movie_length(minutes):
    if minutes > 120:
        return "long"
    elif minutes > 100:
        return "medium"
    else:
        return "short"

if __name__ == "__main__":
    # tasks sorted by the number (second item), smallest first, using sorted and a lambda.
    print(sorted(tasks, key=lambda l: l[1]))
    # tasks sorted by name length, longest first.
    print(sorted(tasks, key=lambda t: len(t[0]), reverse=True))
    # A new column length from a named function you define: 
    # "long" if over 120 minutes, "medium" if over 100, otherwise "short". Print the table.
    movies["length"] = movies["minutes"].apply(movie_length)
    print(movies)

    # A new column era using .apply and a lambda: "new" if the year is 2015 or later, otherwise "old".
    movies["era"] = movies["year"].apply(lambda l: "new" if l >= 2015 else "old")
    
    # A new column hours: minutes divided by 60. Choose the right tool for this one, 
    # and add a one-line comment saying why you chose it.
    # Used column vectorization as we simply needed to convert mins into hours hence this was feasible over lambda/apply
    movies["hours"] = movies["minutes"] / 60  
    print(movies)