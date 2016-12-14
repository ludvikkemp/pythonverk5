import csv
import urllib.request
import codecs
import json
from flask import Flask, render_template, json

app = Flask(__name__)



@app.route('/')
def main():
    
    return render_template('mainMenu.html')


@app.route("/enleaguetable/")
def enleaguetable():
    data = getLeagueTable()
    return render_template('enleaguetable.html', data=data)



def getListOfGames():
    URL = 'http://www.football-data.co.uk/mmz4281/1617/E0.csv'

    response = urllib.request.urlopen(URL)
    listOfGames = [{k : v for k, v in row.items()} for row in
                   csv.DictReader(codecs.iterdecode(response, 'utf-8'), skipinitialspace=True)]
    return listOfGames

def getLeagueTable():
    listOfGames = getListOfGames()
    setOfTeams = set()

    for game in listOfGames:
        setOfTeams.add(game['HomeTeam'])

    teamDict = {}

    for team in setOfTeams:
        #teamDict[team] = {'Games': 0, 'Wins': 0, 'Losses': 0,
        #                   'Draws': 0, 'GoalsScored': 0, 'GoalsConceded': 0,
        #                   'GoalDifference': 0, 'Points': 0}
        teamDict[team] = [0,0,0,0,0,0,0,0]

    for game in listOfGames:
        teamDict[game['HomeTeam']][0] += 1
        teamDict[game['AwayTeam']][0] += 1
        teamDict[game['HomeTeam']][4] += int(game['FTHG'])
        teamDict[game['AwayTeam']][4] += int(game['FTAG'])
        teamDict[game['HomeTeam']][5] += int(game['FTAG'])
        teamDict[game['AwayTeam']][5] += int(game['FTHG'])
        teamDict[game['HomeTeam']][6] += (int(game['FTHG']) - int(game['FTAG']))
        teamDict[game['AwayTeam']][6] += (int(game['FTAG']) - int(game['FTHG']))
        if game['FTR'] == 'H':
            teamDict[game['HomeTeam']][1] += 1
            teamDict[game['HomeTeam']][7] += 3
            teamDict[game['AwayTeam']][2] += 1
        elif game['FTR'] == 'A':
            teamDict[game['AwayTeam']][1] += 1
            teamDict[game['AwayTeam']][7] += 3
            teamDict[game['HomeTeam']][2] += 1
        else:
            teamDict[game['AwayTeam']][3] += 1
            teamDict[game['HomeTeam']][3] += 1
            teamDict[game['AwayTeam']][7] += 1
            teamDict[game['HomeTeam']][7] += 1


    return sorted(teamDict.items(), key=lambda x: (x[1][7], x[1][6]), reverse=True)


if __name__ == "__main__":
    app.run()
    
