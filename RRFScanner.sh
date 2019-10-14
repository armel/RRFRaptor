#!/bin/sh

PATH_SCRIPT='/opt/RRFScanner/RRFScanner.py'
PATH_LOG='/tmp'
PATH_PID='/tmp'

cmd = `/usr/bin/pgrep -f "python /opt/RRFScanner/RRFScanner.py"`

echo $cmd

case "$1" in
    start)
        echo "Starting RRFScanner"
        nohup python $PATH_SCRIPT --room TECHNIQUE --sleep 1  --debug Flase > $PATH_LOG/RRFScanner.log 2>&1 & echo $! > $PATH_PID/RRFScanner.pid
        ;;
    stop) 
        echo "Stopping RRFScanner"
        kill `cat $PATH_PID/RRFScanner.pid`
        ;;
    esac