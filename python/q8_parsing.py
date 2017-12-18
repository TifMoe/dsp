# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import pandas as pd

football = pd.read_csv('football.csv')
football['goals_diff'] = [abs(g - ga) for index, (g, ga) in football[['Goals', 'Goals Allowed']].iterrows()]

smallest_diff = min(football['goals_diff'])
teams = [(goals, team) for (goals, team) in zip(football['goals_diff'], football['Team']) if goals == smallest_diff]

print("{} has the smallest difference in for and against goals".format(' and '.join([i[1] for i in teams])))
