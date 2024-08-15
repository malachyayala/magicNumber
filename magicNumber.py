#!/usr/bin/env python3
from pybaseball import standings
import pandas as pd
import argparse

def getRecords(team_name):
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

def calculateMagicNumber(totalG, teamA, teamB):
    # Assign win and loss values to team A and team B
    aWins = teamA['W'].values[0]
    bLosses = teamB['L']
    
    # Calculate magic number: Total games + 1 - team A wins - team B losses
    magicNumber = int(totalG) + 1 - int(aWins) - int(bLosses)

    return magicNumber

def main():
    # Set up command line argument parsing
    parser = argparse.ArgumentParser(description="Calculate the magic number for a baseball team.")
    parser.add_argument("total_games", type=int, help="The total number of games in the season")
    parser.add_argument("team_name", type=str, help="The name of the team")
    
    args = parser.parse_args()

    # Get record of provided team and the team behind them in the standings
    teamA, teamB = getRecords(args.team_name)
    mn = calculateMagicNumber(args.total_games, teamA, teamB)
    
    print(mn)

if __name__ == "__main__":
    main()