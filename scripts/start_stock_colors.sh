#!/bin/bash
PROJECT_HOME='/home/pi/workspace/lifx/stock_market_lights/my_fork/lifxlan'
PID_FILE="${PROJECT_HOME}/scripts/stock_colors.pid"
touch $PID_FILE
pid=`cat "${PID_FILE}"`
kill $pid
/usr/bin/python3 $PROJECT_HOME/stock_colors.py $1 > /dev/null 2>&1 &
pid=$!
echo "${pid}" > $PID_FILE
