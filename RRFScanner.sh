#!/bin/sh

PATH_SCRIPT='/opt/RRFScanner/RRFScanner.py'
PATH_LOG='/tmp'
PATH_PID='/tmp'

case "$1" in
    start)
        echo "Starting RRFScanner"
        nohup python $PATH_SCRIPT --standby TECHNIQUE --sleep 1  > $PATH_LOG/RRFScanner.log 2>&1 & echo $! > $PATH_PID/RRFScanner.pid
        ;;
    stop) 
        echo "Stopping RRFScanner"
        kill `cat $PATH_PID/RRFScanner.pid`
        ;;
    esac