#!/usr/bin/env python
# coding=utf-8

from yahoo_oauth import OAuth2
from yahoo_fantasy_api import *
import json
import pprint

from functions.yahoo_constants import *
from functions.common_functions import *


APP_NAME="fantasy_colors"


def getOAuth():
    log("Getting OAuth2 authentication...")
    return OAuth2(None, None, from_file=OAUTH_CRED_FILEPATH)


def main():
    set_up_log(APP_NAME)
    log("Starting " + APP_NAME + "...")
    oauth = getOAuth()
    print("League ID: " + LEAGUE_ID)
    print("Game ID: " + GAME_ID)
    
    nfl_game = game.Game(oauth, GAME_ID)
    
    print("League IDs:")
    pprint.pprint(nfl_game.league_ids("2021"))
    league = nfl_game.to_league(LEAGUE_ID)
    
    print("League:")
    pprint.pprint(league)
    
    print("Current Week: " + league.current_week())

    league_standings = league.standings()
    print("league_standings: ")
    pprint.pprint(league_standings)


#atexit.register(exit_handler)
if __name__=="__main__":
    main()
