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
            
        leaguesInSeasons[seasons[seasonsCounter].text.replace('/','-')].append((leagues[leaguesCounter]['href'], leagues[leaguesCounter].text))

        if flag == True:
            flagCounter += 1
        leaguesCounter += 1

    leaguesInSeasonsSorted = sorted(leaguesInSeasons.items(), reverse=True)

    return leaguesInSeasonsSorted

data = mainFetchData()

        
@app.route('/')
def main():
    return render_template('mainMenu.html', data=data)




def getData(seasonLeague):
    for season in data:
        for league in season[1]:
            if season[0] + league[1] == seasonLeague:
                return league[0]
    


@app.route("/leaguetable/<league>")
def leaguetable(league):
    csv = getData(league)
    URL = 'http://www.football-data.co.uk/'+ csv
    tabledata = [getLeagueTable(URL), league[16:],
            getRefereeTable(URL), 'Referee Stats']
    return render_template('enleaguetable.html', data=tabledata)


def getListOfGames(URL):
    response = urllib.request.urlopen(URL)
    listOfGames = [{k : v for k, v in row.items()}
                   for row in csv.DictReader(codecs.iterdecode
                    (response, 'latin1'),skipinitialspace=True)]
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
        if 'HF' in game:    
            refDict[game['Referee']][0] += (int(game['HF'] or 0) + int(game['AF'] or 0))
        refDict[game['Referee']][1] += (int(game['HY'] or 0) + int(game['AY'] or 0))
        refDict[game['Referee']][2] += (int(game['HR'] or 0) + int(game['AR'] or 0))

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
        teamDict[game['HomeTeam']][4] += int(game['FTHG'] or 0)
        teamDict[game['AwayTeam']][4] += int(game['FTAG'] or 0)
        teamDict[game['HomeTeam']][5] += int(game['FTAG'] or 0)
        teamDict[game['AwayTeam']][5] += int(game['FTHG'] or 0)
        teamDict[game['HomeTeam']][6] += (int(game['FTHG'] or 0) - int(game['FTAG'] or 0))
        teamDict[game['AwayTeam']][6] += (int(game['FTAG'] or 0) - int(game['FTHG'] or 0))
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
    
