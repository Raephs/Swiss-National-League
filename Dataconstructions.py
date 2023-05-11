from getdata import *


def teamsandplayers():
    teamsID=getTeams()
    playerID=getplayers()
    player=playerID[0]
    teams=teamsID[0][1]
    jerseylist=[]
    teamid=0
    """""
    for i in range (len(teamsID)):
        print(teamsID[i][teamid])
        continue
    """
    for p in range (len(playerID)):
            playerinfo=playerID[p]
            pvalue = playerinfo[6]
            for t in range (len(teamsID)):
                teamsinfo=teamsID[t]
                teamsnumid=teamsinfo[1]
                tvalue=int(teamsnumid)
                if  int(tvalue)== int(pvalue):
                    print(teamsID[t][0],playerID[p][0],playerID[p][1],playerID[p][2])
    """            
    playerinfo=playerID[0]
    value = playerinfo[6]
    print(int(value))
    """            


teamsandplayers()