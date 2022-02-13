#!/usr/bin/env python
# coding=utf-8
import datetime
import os
import logging
from lifxlan import *
from pathlib import Path
from .common_constants import *

lifxlan = LifxLAN(NUMBER_OF_LIGHTS)

def create_directory(path):
    if not os.path.exists(path):
        print("log directory created")
        os.makedirs(path)

def set_up_log(app_name, logging_level = logging.INFO):
    create_directory(LOG_DIR)
    log_filepath = get_log_filepath(app_name)
    file = Path(log_filepath)
    file.touch(exist_ok=True)
    logging.basicConfig(filename=log_filepath, level=logging_level)

def log(statement):
    log_statement = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\t" + statement
    logging.info(log_statement)


def exit_handler():
    print("Exiting application, turning lights off.")
    lifxlan.set_power_all_lights(OFF)    


def get_percent_difference(current, previous):
    if current == previous:
        percent_difference = 100.0
    try:
        percent_difference = ((current - previous) / previous) * 100.0
    except ZeroDivisionError:
        precent_difference = 0

    log("Percent difference betweeen " + str(current) + " and " + str(previous) + " is " + str(percent_difference))
    return percent_difference


def set_color_all(color, brightness=MAX_VALUE):
    if isinstance(color, int):
        log("Setting color to: " + str(color))
        log("Setting brightness to: " + str(brightness / MAX_VALUE * 100) + "%")
        lifxlan.set_power_all_lights(ON)
        lifxlan.set_color_all_lights([int(round(color)), MAX_VALUE, int(round(brightness)), 9000])
    elif isinstance(color, float):
        set_color_all(color, brightness)
    #elif isinstance(color, RED.__class__.__name__):
    #    print("Color is a LifxLAN color")
    #    lifxlan.set_color_all_lights(color)
    else:
        set_color_all(color[0], brightness)


def normalize_percent_difference_for_color(percent_difference, percentage_range=5):
    log("Noramlizing percent differnce of " + str(percent_difference) + "%")
    log("Using percentage range of " + str(percentage_range) + "%")
    return_value = percent_difference
    if return_value > percentage_range:
        return_value = percentage_range
    elif return_value < -abs(percentage_range):
        return_value = -abs(percentage_range)
    
    return_value = abs(return_value) * MAX_VALUE / percentage_range
    log("Percent difference normalized to " + str(return_value))
    return return_value   




