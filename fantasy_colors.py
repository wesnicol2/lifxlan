#!/usr/bin/env python
# coding=utf-8

from yahoo_oauth import OAuth2
from yahoo_fantasy_api import *
import json

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
    
    # Need to figure out the NFL game code (I think it is one code for the entire sport)
    print("Game IDs: " + str(game.Game(oauth, "371").league_ids()))
    fantasy_league = league.League(oauth, LEAGUE_ID)
    print(fantasy_league.current_week())

    league_standings = fantasy_league.standings()
    print("league_standings: " + str(league_standings))


#atexit.register(exit_handler)
if __name__=="__main__":
    main()
