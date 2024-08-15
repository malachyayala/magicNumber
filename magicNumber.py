from pybaseball import standings
import pandas as pd
totalGames = input("Input total games: ")
team_name = input("Input team name: ")

def getRecords(team):
    currentStandings = standings(2024)
    team_record = None
    next_team_record = None
    for df in currentStandings:
        # Check if the team is in the current DataFrame
        if team_name in df['Tm'].values:
            team_record = df[df['Tm'] == team_name]
            team_index = df[df['Tm'] == team_name].index[0]
            print(team_index)
            print('here')
            if team_index + 1 < len(df):
                next_team_record = df.iloc[team_index]
            break  # Exit the loop once the team is found
    
    return team_record, next_team_record

def main():
    teamA, teamB = getRecords(team_name)
    aWins = teamA['W'].values[0]
    bLosses = teamB['L']
    print(teamA['W'].values[0], teamA['L'].values[0])
    magicNumber = int(totalGames) + 1 - int(aWins) - int(bLosses)
    print(magicNumber)

main()