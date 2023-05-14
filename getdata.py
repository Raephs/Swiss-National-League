import requests
import json

# https://www.nationalleague.ch/api/player/
# https://www.nationalleague.ch/api/teams/
# https://www.nationalleague.ch/api/games/gameid
# https://www.nationalleague.ch/api/teams/101144/logo

API_URL = 'https://www.nationalleague.ch/api/%s/'

def getPlayers():
    response = requests.get(API_URL % 'player')
    responseData = response.json()

    players = []

    for data in responseData:
        player = [
            data['firstName'],
            data['lastName'],
            data['number'],
            data['nationality'],
            data['position'],
            data['playerId'],
            data['teamId'],
            data['topscorerPoints'],
            data['topscorerPointAverage'],
            data['topscorerMarketValue']
        ]
        players.append(player)

    return players

def getPlayersInfo():
    players = getPlayers()
    with open('playerinfo.json', 'w') as fp:
        json.dump(players, fp, 7)

def getTeams():
    response = requests.get(API_URL % 'teams')
    responseData = response.json()
    
    teams = []

    for data in responseData:
        team = [
            data['name'],
            data['teamId'],
            data['website']
        ];
        teams.append(team)
    
    return teams

def getTeamsInfo():
    teamsInfo = getTeams()
    with open('teamsinfo.json', 'w') as fp:
        json.dump(teamsInfo, fp, 4)


def getGames():
    response = requests.get(API_URL % 'games')
    responseData = response.json()

    games = [];

    for data in responseData:
        game = [
            data['gameId'],
            data['date'],
            data['homeTeamId'],
            data['homeTeamResult'],
            data['awayTeamId'],
            data['awayTeamResult'],
        ];
        games.append(game)
        
    return games  

def getGamesInfo():
    gamesInfo = getGames()
    with open('gamesinfo.json', 'w') as fp:
        json.dump(gamesInfo, fp, 5)

def getGameStat(gameID: int):
    response = requests.get(API_URL % ('games') + str(gameID))
    responseData = response.json()
    for dataGameStat, value in responseData.items():
        print(dataGameStat, ' -> ', value)
    

gameID = 20236105000070
getGameStat(gameID)