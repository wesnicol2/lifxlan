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
import traceback
from functions.common_constants import * 
from functions.common_functions import *
import functions.stock_constants as stock_constants
from retrying import retry

APP_NAME = "stock_colors"
DOW_JONES_AVERAGE = "^DJA"
lifxlan = LifxLAN(NUMBER_OF_LIGHTS)
MAX_RETRIES = 100
#LIGHT_1_MAC_ADDRESS = "d0:73:d5:69:7f:33"
#LIGHT_1_IP_ADDRESS = "192.168.0.2"
#LIGHT_2_MAC_ADDRESS = "d0:73:d5:6b:80:bb"
#LIGHT_2_IP_ADDRESS = "192.168.0.91"



def getStockChangeToday(ticker):
    info=yf.Ticker(ticker).info
    primary_current_price_key = stock_constants.RM_CURRENT_PRICE
    secondary_current_price_key = stock_constants.RM_CURRENT_PRICE
    primary_starting_price_key = stock_constants.RM_CLOSE_PRICE
    secondary_starting_price_key = stock_constants.OPEN_PRICE    

    try:
        current_price = info[primary_current_price_key]
        current_price_type = primary_current_price_key
    except:
        log("Could not retrieve " + str(primary_current_price_key) + " key from stock info object for ticker " + str(ticker))
        log ("Trying with " + str(secondary_current_price_key) + " instead")
        current_price = info[secondary_current_price_key] 
        current_price_type = secondary_current_price_key

    try:
        starting_price = info[primary_starting_price_key]
        starting_price_type = primary_starting_price_key

    except: 
        log("Could not retrieve " + str(primary_starting_price_key) + " key from stock info object for ticker " + str(ticker))
        log ("Trying with " + str(secondary_starting_price_key) + " instead")
        starting_price = info[secondary_starting_price_key]
        starting_price_type = secondary_starting_price_key

    log(str(ticker) + " starting price (from '" + str(starting_price_type) + "' key):\t$" + str(starting_price))
    log(str(ticker) + " current price(from '" + str(current_price_type) + "' key):\t\t$" + str(current_price))

    return get_percent_difference(current_price, starting_price)


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
    

@retry(stop_max_attempt_number=MAX_RETRIES)
def main():
    set_up_log(APP_NAME)
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
            set_color_all(color, normalized)

    except:
        log("Exception encounted:")
        log(traceback.format_exc())

        exit()
        
    #light1 = Light(LIGHT_1_MAC_ADDRESS, LIGHT_1_IP_ADDRESS)
    #light2 = Light(LIGHT_2_MAC_ADDRESS, LIGHT_2_IP_ADDRESS)
      
    
atexit.register(exit_handler)
if __name__=="__main__":
    main()


