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

APP_NAME = "stock_colors"
DOW_JONES_AVERAGE = "^DJA"
lifxlan = LifxLAN(NUMBER_OF_LIGHTS)

#LIGHT_1_MAC_ADDRESS = "d0:73:d5:69:7f:33"
#LIGHT_1_IP_ADDRESS = "192.168.0.2"
#LIGHT_2_MAC_ADDRESS = "d0:73:d5:6b:80:bb"
#LIGHT_2_IP_ADDRESS = "192.168.0.91"



def getStockChangeToday(ticker):
    info=yf.Ticker(ticker).info
    current_price = info['regularMarketPrice']
    log("Current Price: " + str(current_price))
    open_price = info['regularMarketPreviousClose']
    log("Day open price: " + str(open_price))
    return get_percent_difference(current_price, open_price)


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
            set_color_all(color, normalize_percent_difference_for_color(percent_difference))

    except:
        log("Exception encounted:")
        log(traceback.format_exc())
        exit()
        
    #light1 = Light(LIGHT_1_MAC_ADDRESS, LIGHT_1_IP_ADDRESS)
    #light2 = Light(LIGHT_2_MAC_ADDRESS, LIGHT_2_IP_ADDRESS)
      
    
atexit.register(exit_handler)
if __name__=="__main__":
    main()


