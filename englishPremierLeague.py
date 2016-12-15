import csv
import urllib.request
import codecs
import json
from flask import Flask, render_template, json
from bs4 import BeautifulSoup
from collections import defaultdict

app = Flask(__name__)

def mainFetchData():
    url = 'http://www.football-data.co.uk/englandm.php'
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    
    tableRow = soup.find_all('td', attrs={'valign':'top'})[2]

    seasons = tableRow.find_all('i')[1:]
    leagues = tableRow.find_all('a')[6:-1]

    seasonsCounter = 0
    leaguesCounter = 0
    numberOfLeaguesInSeason = 5
    leaguesInSeasons = defaultdict(list)
    flag = False
    flagCounter = 0
    for league in leagues:
        if seasonsCounter == 11:
            numberOfLeaguesInSeason = 4
            flag = True

        if (leaguesCounter % numberOfLeaguesInSeason) == 0 and leaguesCounter != 0 and flag == False:
            seasonsCounter += 1
        if (flagCounter % numberOfLeaguesInSeason) == 0 and flagCounter != 0 and flag == True:
            seasonsCounter += 1
            
        leaguesInSeasons[seasons[seasonsCounter].text].append((leagues[leaguesCounter]['href'], leagues[leaguesCounter].text))

        if flag == True:
            flagCounter += 1
        leaguesCounter += 1

    leaguesInSeasonsSorted = sorted(leaguesInSeasons.items(), reverse=True)

    return leaguesInSeasonsSorted

        
@app.route('/')
def main():
    data = mainFetchData()
    return render_template('mainMenu.html', data=data)


@app.route("/enleaguetable/<csv>")
def enleaguetable(csv):
    URL = 'http://www.football-data.co.uk/' + csv
    data = [getLeagueTable(URL), 'English Premier League Table 2016-17',
            getRefereeTable(URL), 'EPL Referee Stats Table 2016-17']
    return render_template('enleaguetable.html', data=data)

@app.route("/championship/")
def championshiptable():
    URL = 'http://www.football-data.co.uk/mmz4281/1617/E1.csv'
    data = [getLeagueTable(URL), 'Championship Table 2016-17',
            getRefereeTable(URL), 'Championship Referee Stats Table 2016-17']
    return render_template('enleaguetable.html', data=data)


def getListOfGames(URL):
    response = urllib.request.urlopen(URL)
    listOfGames = [{k : v for k, v in row.items()}
                   for row in csv.DictReader(codecs.iterdecode
                    (response, 'utf-8'),skipinitialspace=True)]
    return listOfGames

def getRefereeTable(URL):
    listOfGames = getListOfGames(URL)
    setOfRefs = set()

    for game in listOfGames:
        setOfRefs.add(game['Referee'])

    refDict = {}

    for ref in setOfRefs:
        refDict[ref] = [0,0,0]

    for game in listOfGames:
        refDict[game['Referee']][0] += (int(game['HF']) + int(game['AF']))
        refDict[game['Referee']][1] += (int(game['HY']) + int(game['AY']))
        refDict[game['Referee']][2] += (int(game['HR']) + int(game['AR']))

    return sorted(refDict.items(), key=lambda x: (x[1][2], x[1][1], x[1][0]), reverse=True)

def getLeagueTable(URL):
    listOfGames = getListOfGames(URL)

    setOfTeams = set()
    
    for game in listOfGames:
        setOfTeams.add(game['HomeTeam'])

    teamDict = {}

    for team in setOfTeams:
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
    
