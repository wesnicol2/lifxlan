#!/usr/bin/env python
# coding=utf-8


from functions.yahoo_constants import *
from functions.common_functions import *

APP_NAME="fantasy_colors"


def main():
    set_up_log(APP_NAME)
    log("Starting " + APP_NAME + "...")


atexit.register(exit_handler)
if __name__=="__main__":
    main()
