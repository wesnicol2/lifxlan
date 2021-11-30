#!/usr/bin/env python
# coding=utf-8

import functools

class Team:
    wins = []
    losses = []
    points = 0

    # constructor for the with the team id and name
    def __init__(self, id, name):
        self.id = id
        self.name = name

APP_NAME="playoff_calculator"


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
        print("Enter point values for " + team1.name + " and " + team2.name)
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

    teams[0].points = 1365.64
    teams[1].points = 1333.58
    teams[5].points = -1


    teams[0].wins = [10, 7, 6, 4, 9, 8, 2]   
    teams[0].losses = [8, 2, 3, 5]
    teams[1].wins = [1, 6, 9, 8, 5, 10, 7]
    teams[1].losses = [7, 4, 3, 1]
    teams[2].wins = [10, 7, 1, 6, 2, 10, 5]   
    teams[2].losses = [5, 4, 9, 8]
    teams[3].wins = [9, 2, 10, 3, 6, 5, 9]
    teams[3].losses = [5, 8, 7, 1]
    teams[4].wins = [4, 3, 9, 8, 1]   
    teams[4].losses = [7, 2, 6, 10, 4, 3]
    teams[5].wins = [9, 10, 5, 9, 8]
    teams[5].losses = [8, 2, 3, 7, 1, 4]
    teams[6].wins = [2, 10, 5, 6, 4]   
    teams[6].losses = [3, 1, 9, 8, 2, 10]
    teams[7].wins = [1, 6, 4, 3, 7]
    teams[7].losses = [9, 5, 2, 10, 1, 6]
    teams[8].wins = [8, 10, 3, 7]   
    teams[8].losses = [6, 4, 5, 2, 1, 6, 4]
    teams[9].wins = [8, 5, 7]
    teams[9].losses = [3, 7, 1, 6, 4, 9, 2, 3]
      
    teams = sorted(teams, key=functools.cmp_to_key(compareTeams))

    #print teams in order
    i = 1
    for team in teams:
        print(str(i) + "\t" + team.name)
        if i == 6:
            print("\n")
        i += 1
        
#atexit.register(exit_handler)
if __name__=="__main__":
    main()
