import numpy as np

step_count = np.array([4200, 11500, 8000, 15200, 3000, 9800, 12000])

if __name__ == "__main__":
    
    # Boolean mask of days with with atleast 10000 steps
    goal_met = step_count >= 10000
    print(goal_met)
    # The step counts on those days.
    print(step_count[goal_met])
    # How many days hit at least 10,000.
    print((goal_met).sum())
    # The step counts between 5,000 and 10,000 inclusive on both ends.
    print(step_count[(step_count >= 5000) & (step_count <= 10000)])
    # The step counts on days that were not above 5,000.
    print(step_count[~(step_count > 5000)])
    # The average of the days that hit at least 10,000.
    print((step_count[goal_met]).mean())