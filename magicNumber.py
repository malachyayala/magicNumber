from pybaseball import standings
import pandas as pd
standings = standings(2024)
team_record = None
next_team_record = None
totalGames = input("Input total games: ")
team_name = input("Input team name: ")

for df in standings:
    # Check if the team is in the current DataFrame
    if team_name in df['Tm'].values:
        team_record = df[df['Tm'] == team_name]
        team_index = df[df['Tm'] == team_name].index[0]
        if team_index + 1 < len(df):
            next_team_record = df.iloc[team_index + 1]
        break  # Exit the loop once the team is found

aWins = team_record['W'].values[0]
bLosses = next_team_record['L']
print(team_record['W'].values[0], team_record['L'].values[0])
print(next_team_record['W'], next_team_record['L'])
1
magicNumber = int(totalGames) + 1 - int(aWins) - int(bLosses)
print(magicNumber)