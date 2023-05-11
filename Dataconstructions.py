from getdata import *

#lists Team and their players
def teamsandplayers():
    teamsID=getTeams()
    playerID=getplayers()
    for p in range (len(playerID)):
            playerinfo=playerID[p]
            pvalue = playerinfo[6]
            for t in range (len(teamsID)):
                teamsinfo=teamsID[t]
                teamsnumid=teamsinfo[1]
                tvalue=int(teamsnumid)
                if  int(tvalue)== int(pvalue):
                    print(teamsID[t][0],playerID[p][0],playerID[p][1],playerID[p][2])
      
teamsandplayers()