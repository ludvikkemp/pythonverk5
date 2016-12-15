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
leagues and calculates the results. The results are the calculated and displayed
as the league table stands.

All the data is comes in a csv file. An example csv file comes in the project directory
and is called E0.csv if you want to look at the data

Notes for Football Data

All data is in csv format, ready for use within standard spreadsheet applications. Please note that some abbreviations are no longer in use (in particular odds from specific bookmakers no longer used) and refer to data collected in earlier seasons. For a current list of what bookmakers are included in the dataset please visit [football-data.co.uk](http://www.football-data.co.uk/matches.php)

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
