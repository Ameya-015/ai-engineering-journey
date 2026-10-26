import numpy as np

raw = [30, 45,  0, 60, 20, 90, 15,
        0, 10, 20,  0, 35, 40, 50,
       60, 60, 75, 80, 45,  0, 30,
       15,  0,  0, 25, 10,  5, 20]

usage_minutes = np.array(raw).reshape(4, -1)

# user_totals(usage): each user’s weekly total, as a column vector.
def user_totals(usage):
    total = usage.sum(axis=1, keepdims=True)
    return total

# daily_averagess(usage): the average minutes per day across users.
def daily_averages(usage):
    avg_mins_per_day = usage.mean(axis=0)
    return avg_mins_per_day

# active_days(usage, threshold=30): per user, how many days they hit at least threshold minutes.
def active_days(usage, threshold=30):
    return (usage >= threshold).sum(axis=1)

# top_user(usage): the index of the user with the highest weekly total.
def top_user(usage):
    return usage.sum(axis=1).argmax()

# weekly_share(usage): each value as a fraction of that user’s weekly total, so each row sums to 1. Reuse user_totals.
def weekly_share(usage):
    weekly_total = user_totals(usage)
    return (usage / weekly_total)

# centered_by_day(usage): each value minus that day’s average. Reuse daily_averagess.
def centered_by_day(usage):
    per_day_avg = daily_averages(usage)
    return (usage - per_day_avg)

# zero_days(usage): the total number of user-days with zero usage, across everyone.
def zero_days(usage):
    return (usage == 0).sum()

if __name__ == "__main__":
    total_per_student = user_totals(usage_minutes)
    print(f"User totals:\n{total_per_student}")

    avg_per_day = daily_averages(usage_minutes)
    print(f"Daily average: {avg_per_day}")

    number_of_activedays = active_days(usage_minutes, 30)
    print(f"Active days with 30 mins spent on app: {number_of_activedays}")

    sixty_mins_per_day = active_days(usage_minutes, 60)
    print(f"Active days 60 mins spent on app: {sixty_mins_per_day}")

    top_user_index = top_user(usage_minutes)
    print(f"Top user: {top_user_index}")

    weekly_avg = weekly_share(usage_minutes)
    print(f"Weekly share:\n {weekly_avg}")

    avg_diff_per_day = centered_by_day(usage_minutes)
    print(f"Per day difference with average: {avg_diff_per_day}")

    zero_mins_spent = zero_days(usage_minutes)
    print(f"Total number of days with zero usage: {zero_mins_spent}")