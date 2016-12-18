# Python Project 5

## Displaying All League Tables in English Football

### Before runnig the script Flask and BeautifulSoup are required
-------------------------------------------------------------

### How to install required packages
#### Run the following commands in your Terminal/Command Prompt

For Windows:
* Flask: py -m pip install flask
* BeautifulSoup: py -m pip install BeautifulSoup4

For Linux and Mac:
* Flask: pyhton3 -m pip install flask
* BeautifulSoup: python3 -m pip install BeautifulSoup4

==============================================================

### After installation run the script in your Terminal/Command Prompt:

* Windows: py footballLeagues.py
* Linux/Mac: python3 footballLeagues.py

### When the script is runnig you should see following text:

Running on http://PORT_NUMBER/ (Press CTRL+C to quit)


## How the script works:
The program fetches information on every football match played in all the English
leagues and calculates results. The results are the displayed in a table in the html
files. All information is automatically updated when the website that provites the
data is updated.

The first step is to take all the data from the csv file and read it into a list of dictionaries. So basically
we have a list of every football game in that particular league. Each list item has a key and a value for examlpe:
{'HomeTeam' : 'Liverpool'}

The script iterates through every game to gather data for each team to keep count of points, goals, wins etc
and displayes the current state of a certain league table. It does so not only to leagues that are still being
played but also from previous years.

There is so much info on each game that the possibilities for making all kinds of stats are almost endless.
A list og explaination for a few of them can be found later in this document. We decided to include a list
of referees sorted by how strict they are. Firstly on red card, then on yellow card and finally on how many
fouls they gave. No real reason for that exactly except to furfill our own curiousity :)

There is no data on referee stats for seasons 1993-1999 so the table is empty.

## Notes for Football Data

All data is in csv format, ready for use within standard spreadsheet applications. Please note that some abbreviations are no longer in use (in particular odds from specific bookmakers no longer used) and refer to data collected in earlier seasons. For a current list of what bookmakers are included in the dataset please visit [football-data.co.uk](http://www.football-data.co.uk/matches.php)

An example csv file comes in the project directory band is called E0.csv if you want to look at the data

#### Key to results data:

* Div = League Division
* Date = Match Date (dd/mm/yy)
* HomeTeam = Home Team
* AwayTeam = Away Team
* FTHG = Full Time Home Team Goals
* FTAG = Full Time Away Team Goals
* FTR = Full Time Result (H=Home Win, D=Draw, A=Away Win)
* HTHG = Half Time Home Team Goals
* HTAG = Half Time Away Team Goals
* HTR = Half Time Result (H=Home Win, D=Draw, A=Away Win)

#### Match Statistics (where available)
* Attendance = Crowd Attendance
* Referee = Match Referee
* HS = Home Team Shots
* AS = Away Team Shots
* HST = Home Team Shots on Target
* AST = Away Team Shots on Target
* HHW = Home Team Hit Woodwork
* AHW = Away Team Hit Woodwork
* HC = Home Team Corners
* AC = Away Team Corners
* HF = Home Team Fouls Committed
* AF = Away Team Fouls Committed
* HO = Home Team Offsides
* AO = Away Team Offsides
* HY = Home Team Yellow Cards
* AY = Away Team Yellow Cards
* HR = Home Team Red Cards
* AR = Away Team Red Cards

### Files in Project

* E0.csv
* footballLeagues.py
* README.md
* templates/enleaguetable.html
* templates/mainMenu.html