#!/usr/bin/env python
# coding=utf-8
import sys
import os
from time import sleep
import yfinance as yf
import atexit
import logging
from lifxlan import *
from pathlib import Path


ON=1
OFF=0
NUMBER_OF_LIGHTS = 2
MAX_VALUE = 65535
DOW_JONES_AVERAGE = "^DJA"
lifxlan = LifxLAN(NUMBER_OF_LIGHTS)
PROJECT_HOME='/home/pi/workspace/lifx/stock_market_lights/my_fork/lifxlan'
LOG_DIR = PROJECT_HOME + '/log'
LOG_FILE = LOG_DIR + '/stock_colors_' + datetime.now().strftime("%Y%m%d") + '.log'

#LIGHT_1_MAC_ADDRESS = "d0:73:d5:69:7f:33"
#LIGHT_1_IP_ADDRESS = "192.168.0.2"
#LIGHT_2_MAC_ADDRESS = "d0:73:d5:6b:80:bb"
#LIGHT_2_IP_ADDRESS = "192.168.0.91"


def create_directory(path):
    if not os.path.exists(path):
        print("log directory created")
        os.makedirs(path)

def set_up_log(logging_level = logging.INFO):
    create_directory(LOG_DIR)
    file = Path(LOG_FILE)
    file.touch(exist_ok=True)
    logging.basicConfig(filename=LOG_FILE, level=logging_level)

def log(statement):
    logging.info(statement)


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

def getStockChangeToday(ticker):
    info=yf.Ticker(ticker).info
    current_price = info['regularMarketPrice']
    log("Current Price: " + str(current_price))
    open_price = info['open']
    log("Day open price: " + str(open_price))
    return get_percent_difference(current_price, open_price)


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
        
        
def print_usage():
    print("USAGE: python3 stock_colors.py <ticker_symbol>")
    print("You can select a ticker symbol from the list on this webapage: http://batstrading.com/market_data/listed_symbols/")
        

def valid_ticker(ticker):
    if yf.Ticker(ticker).info["regularMarketPrice"] is 0:
        log("Ticker " + ticker + " is not valid.")
        return False
    else:
        log("Ticker " + ticker + " is valid.")
        return True
    
def normalize_percent_difference_for_color(percent_difference):
    log("Noramlizing percent differnce of " + str(percent_difference) + "%")
    percentage_range = 5 #percent
    return_value = abs(percent_difference) * MAX_VALUE / percentage_range
    log("Percent difference normalized to " + str(return_value))
    return return_value   
    
    
    
    
    
def main():
    set_up_log()
    log("Starting program...")
    try:
        while True:
            if len(sys.argv) == 1:
                percent_difference = getStockChangeToday(DOW_JONES_AVERAGE)
            elif len(sys.argv) > 2:
                print_usage()
                exit()
            elif not valid_ticker(sys.argv[1]):
                log("That ticker is not listed. Please choose from a value in the following webpage: http://batstrading.com/market_data/listed_symbols/")
                exit()
            else:
                percent_difference = getStockChangeToday(sys.argv[1])

            if percent_difference < 0.0:
                color = RED
            else:
                color = GREEN
        
            normalized = normalize_percent_difference_for_color(percent_difference)
            set_color_all(color, normalize_percent_difference_for_color(percent_difference))

    except Exception as e:
        log("Exception encounted:")
        log(e)
        exit()
        
    #light1 = Light(LIGHT_1_MAC_ADDRESS, LIGHT_1_IP_ADDRESS)
    #light2 = Light(LIGHT_2_MAC_ADDRESS, LIGHT_2_IP_ADDRESS)
      
    
atexit.register(exit_handler)
if __name__=="__main__":
    main()


