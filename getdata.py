import requests
import json

#https://www.nationalleague.ch/api/player/
#https://www.nationalleague.ch/api/teams/
#https://www.nationalleague.ch/api/teams/
#https://www.nationalleague.ch/api/games/
#https://www.nationalleague.ch/api/games/gameid
#https://www.nationalleague.ch/api/teams/101144/logo
###URl
URL= 'https://www.nationalleague.ch/api/teams/'
URL= 'https://www.nationalleague.ch/api/player/'
URL= 'https://www.nationalleague.ch/api/games/'

def getplayers():
    URL= 'https://www.nationalleague.ch/api/player/'
    response = requests.get(URL)
    dataplayers =response.json()

    playersinf_list=[]

    for obj in dataplayers:
        firstname=obj['firstName']
        lastname= obj['lastName']
        playernumber=obj['number']
        nationality=obj['nationality']
        playerposition=obj['position']
        playerId=obj['playerId']
        teamid=obj['teamId']
        topscorerpoints=obj['topscorerPoints']
        topscorerpointaverage=obj['topscorerPointAverage']
        topscorermarketvalue=obj['topscorerMarketValue']

        playersinf_list.append([firstname,lastname,playernumber,nationality,playerposition,playerId,teamid,topscorerpoints,topscorerpointaverage,topscorermarketvalue])
    return playersinf_list

def getplayersinfo():
    playersinf=getplayers()
    with open("playerinfo.json", "w") as fp:
        json.dump(playersinf, fp, indent= 7)

def getTeams():
    url = 'https://www.nationalleague.ch/api/teams/'
    response = requests.get(url)
    teams = response.json()
    
    teaminf_list = []
    
    for team in teams:
        name = team['name']
        id = team['teamId']
        website = team['website']
        
        teaminf_list.append([name, id, website])
    
    return teaminf_list

def getTeamsInfo():
    teaminfo = getTeams()
    with open('teamsinfo.json', 'w') as fp:
        json.dump(teaminfo, fp, indent=4)


def getgames():
    URL= 'https://www.nationalleague.ch/api/games/'
    response = requests.get(URL)
    datagames = response.json()

    gameinf_list=[]
    for obj in datagames:
        gameId=obj['gameId']
        date=obj['date']
        homeTeamId=obj['homeTeamId']
        hometeamresult=obj['homeTeamResult']   
        awayteamId=obj['awayTeamId']
        awayteamresult=obj['awayTeamResult']
        gameinf_list.append([gameId,date,homeTeamId,hometeamresult,awayteamId,awayteamresult])
        
    return gameinf_list    

def getgamesinfo():
    gamesinfo=getgames()
    with open("gamesinfo.json", "w") as fp:
        json.dump(gamesinfo, fp, indent= 5)

def getgamestat(gameID):
    URL= 'https://www.nationalleague.ch/api/games/'
    response= requests.get(URL+gameID)
    gamestats=response.json()
    for obj in gamestats:
        for i in range(len(gamestats)):
            overview=obj[i]
            print(overview)

    

gameID= '20236105000070'
getgamestat(gameID)    
