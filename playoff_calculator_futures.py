#!/usr/bin/env python
# coding=utf-8

import copy
import functools

class Team:
    wins = []
    losses = []
    points = 0

    # constructor for the with the team id and name
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def getRecord(self):
        return (str(len(self.wins)) + "-" + str(len(self.losses)))

APP_NAME="playoff_calculator"

def getBinaryArray(number, bits):
    binaryArray = []
    for i in range(bits):
        binaryArray.append(number % 2)
        number = number // 2
    return binaryArray

def getTeamById(teams, id):
    for team in teams:
        if team.id == id:
            return team
    return None

def playGame(teams, team1Id, team2Id, whichTeamWon):
    if whichTeamWon == 1:
        getTeamById(teams, team1Id).wins.append(team2Id)
        getTeamById(teams, team2Id).losses.append(team1Id)
    else:
        getTeamById(teams, team1Id).losses.append(team2Id)
        getTeamById(teams, team2Id).wins.append(team1Id)

def printTeamsInOrder(teams):
    i = 1
    for team in teams:
        print(str(i) + "\t" + team.name + " " + team.getRecord())
        if i == 6:
            print("\n")
        i += 1

def compareTeams(team1, team2):

    if team1.id == 8:
        return 1 # Gaza Strip Club is always last
    elif team2.id == 8:
        return -1
    elif len(team1.wins) > len(team2.wins):
        return -1
    elif len(team1.wins) < len(team2.wins):
        return 1
    elif team1.wins.count(team2.id) > team2.wins.count(team1.id):
        return -1
    elif team1.wins.count(team2.id) < team2.wins.count(team1.id):
        return 1
    elif team1.points > team2.points:
        return -1
    elif team1.points < team2.points:
        return 1
    else:
        team1.points = int(input("Enter " + team1.name + " points: "))
        team2.points = int(input("Enter " + team2.name + " points: "))
        return 0




def main():
    teams = [
        Team(1, "JV District Champion 2012"),
        Team(2, "The 85ers"),
        Team(3, "ODB's Cleveland Steamers"),
        Team(4, "The Wrong Football"),
        Team(5, "JV"),
        Team(6, "Wokington Football Team"),
        Team(7, "Anti-Daks"),
        Team(8, "Gaza Strip Club"),
        Team(9, "Sgt. Butter"),
        Team(10, "Breezy")
    ]




    getTeamById(teams, 1).wins = [10, 7, 6, 4, 9, 8, 2]   
    getTeamById(teams, 1).losses = [8, 2, 3, 5, 10]
    getTeamById(teams, 1).points = 1365
    getTeamById(teams, 2).wins = [1, 6, 9, 8, 5, 10, 7, 6]
    getTeamById(teams, 2).losses = [7, 4, 3, 1]
    getTeamById(teams, 2).points = 1333
    getTeamById(teams, 3).wins = [10, 7, 1, 6, 2, 10, 5, 7]   
    getTeamById(teams, 3).losses = [5, 4, 9, 8]
    getTeamById(teams, 3).points = 1287
    getTeamById(teams, 4).wins = [9, 2, 10, 3, 6, 5, 9, 8]
    getTeamById(teams, 4).losses = [5, 8, 7, 1]
    getTeamById(teams, 4).points = 1075
    getTeamById(teams, 5).wins = [4, 3, 9, 8, 1]   
    getTeamById(teams, 5).losses = [7, 2, 6, 10, 4, 3, 9]
    getTeamById(teams, 5).points = 1260
    getTeamById(teams, 6).wins = [9, 10, 5, 9, 8]
    getTeamById(teams, 6).losses = [8, 2, 3, 7, 1, 4, 2, 10]
    getTeamById(teams, 6).points = 0
    getTeamById(teams, 7).wins = [2, 10, 5, 6, 4]   
    getTeamById(teams, 7).losses = [3, 1, 9, 8, 2, 10, 3]
    getTeamById(teams, 7).points = 1115
    getTeamById(teams, 8).wins = [1, 6, 4, 3, 7]
    getTeamById(teams, 8).losses = [9, 5, 2, 10, 1, 6, 4]
    getTeamById(teams, 8).points = 1054
    getTeamById(teams, 9).wins = [8, 10, 3, 7, 5]   
    getTeamById(teams, 9).losses = [6, 4, 5, 2, 1, 6, 4]
    getTeamById(teams, 9).points = 1266
    getTeamById(teams, 10).wins = [8, 5, 7, 1]
    getTeamById(teams, 10).losses = [3, 7, 1, 6, 4, 9, 2, 3]
    getTeamById(teams, 10).points = 1038
      
    rankedTeams = sorted(teams, key=functools.cmp_to_key(compareTeams))
    gamesLeft = 4
    
    i = 0
    while i < 2**gamesLeft:
        teamsTemp = copy.deepcopy(teams)
        binaryArray = getBinaryArray(i, gamesLeft)
        playGame(teamsTemp, 6, 10, 0) # If wokeington loses
        playGame(teamsTemp, 3, 1, binaryArray[0])
        playGame(teamsTemp, 7, 5, binaryArray[1])
        playGame(teamsTemp, 4, 2, binaryArray[2])
        playGame(teamsTemp, 9, 8, binaryArray[3])
        rankedTeams = sorted(teamsTemp, key=functools.cmp_to_key(compareTeams))
        if ( (rankedTeams[0].id == 6 or rankedTeams[1].id == 6 or rankedTeams[2].id == 6 or rankedTeams[3].id == 6 or rankedTeams[4].id == 6 or rankedTeams[5].id == 6)):
            print("You made the playoffs!")
            print("Teams who won week 13: ")
            # if(binaryArray[0] == 1):
                # print(getTeamById(teams, 6).name)
            # else:
                # print(getTeamById(teams, 10).name)
            if(binaryArray[0] == 1):
                print(getTeamById(teams, 3).name)
            else:
                print(getTeamById(teams, 1).name)
            if(binaryArray[1] == 1):
                print(getTeamById(teams, 7).name)  
            else:
                print(getTeamById(teams, 5).name)
            if(binaryArray[2] == 1):
                print(getTeamById(teams, 4).name)
            else:
                print(getTeamById(teams, 2).name)
            if(binaryArray[3] == 1):
                print(getTeamById(teams, 9).name)  
            else:
                print(getTeamById(teams, 8).name)
            print("\n\n\n")
        i += 1
        
#atexit.register(exit_handler)
if __name__=="__main__":
    main()
