#!/usr/bin/env python
# coding=utf-8

from datetime import datetime

ON=1
OFF=0
NUMBER_OF_LIGHTS = 2
MAX_VALUE = 65535
PROJECT_HOME='/home/pi/workspace/lifx/stock_market_lights/my_fork/lifxlan'
LOG_DIR = PROJECT_HOME + '/log'
LIFX_COLORS = {
    'red': 0,
    'orange': 35,
    'gold': 47,
    'yellow': 50,
    'green': 100,
    'teal': 180,
    'blue': 110,
    'purple': 270,
    'pink': 290,
}



def get_log_filepath(app_name):
    return LOG_DIR + "/" + app_name + "_" + datetime.now().strftime("%Y%m%d") + ".log"
