#!/usr/bin/env python
# coding=utf-8
import sys
import os
import atexit
import logging
from lifxlan import *
from pathlib import Path
import common_constants

def create_directory(path):
    if not os.path.exists(path):
        print("log directory created")
        os.makedirs(path)

def set_up_log(app_name, logging_level = logging.INFO):
    create_directory(common_constants.LOG_DIR)
    log_filepath = common_constants.get_log_filepath(app_name)
    file = Path(log_filepath)
    file.touch(exist_ok=True)
    logging.basicConfig(filename=log_filepath, level=logging_level)

def log(statement):
    log_statement = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\t" + statement
    logging.info(log_statement)


def exit_handler():
    print("Exiting application, turning lights off.")
    lifxlan.set_power_all_lights(common_constatns.OFF)    


def get_percent_difference(current, previous):
    if current == previous:
        percent_difference = 100.0
    try:
        percent_difference = ((current - previous) / previous) * 100.0
    except ZeroDivisionError:
        precent_difference = 0

    log("Percent difference betweeen " + str(current) + " and " + str(previous) + " is " + str(percent_difference))
    return percent_difference


def set_color_all(color, brightness=common_constants.MAX_VALUE):
    if isinstance(color, int):
        log("Setting color to: " + str(color))
        log("Setting brightness to: " + str(brightness / common_constants.MAX_VALUE * 100) + "%")
        lifxlan.set_power_all_lights(common_constants.ON)
        lifxlan.set_color_all_lights([int(round(color)), common_constants.MAX_VALUE, int(round(brightness)), 9000])
    elif isinstance(color, float):
        set_color_all(color, brightness)
    #elif isinstance(color, RED.__class__.__name__):
    #    print("Color is a LifxLAN color")
    #    lifxlan.set_color_all_lights(color)
    else:
        set_color_all(color[0], brightness)


def normalize_percent_difference_for_color(percent_difference, percentage_range=5):
    log("Noramlizing percent differnce of " + str(percent_difference) + "%")
    return_value = abs(percent_difference) * common_constants.MAX_VALUE / percentage_range
    log("Percent difference normalized to " + str(return_value))
    return return_value   




