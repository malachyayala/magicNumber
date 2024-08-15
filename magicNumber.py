from pybaseball import standings
import pandas as pd

totalGames = input("Input total games: ")
team_name = input("Input team name: ")

def getRecords(team):
    # Get standings
    currentStandings = standings(2024)

    # Initialize team records 
    team_record = None
    next_team_record = None

    # Iterate through the list of dataframes
    for df in currentStandings:
        # Check if the team is in the current DataFrame
        if team_name in df['Tm'].values:
            # Get team A record and index
            team_record = df[df['Tm'] == team_name]
            team_index = df[df['Tm'] == team_name].index[0]

            # Get the following team's, team B, record
            if team_index + 1 < len(df):
                next_team_record = df.iloc[team_index]
            break  # Exit the loop once the team is found
    
    return team_record, next_team_record

def main():
    # Get record of provided team and the team behind them in the standings
    teamA, teamB = getRecords(team_name)

    # Assign win and loss values to team A and team B
    aWins = teamA['W'].values[0]
    bLosses = teamB['L']

    # Calculate magic number: Total games + 1 - team A wins - team B losses
    magicNumber = int(totalGames) + 1 - int(aWins) - int(bLosses)
    
    print(magicNumber)

main()