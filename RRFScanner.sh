#!/bin/sh

PATH_SCRIPT='/opt/RRFScanner/RRFScanner.py'
PATH_LOG='/tmp'
PATH_PID='/tmp'

# Si pas d'argument, on gere tout seul
if [ -z "$1" ]; then
	/usr/bin/pgrep -f 'python /opt/RRFScanner/RRFScanner.py'
	pid=$?
	if [ $pid != 1 ]; then
        cp /opt/RRFScanner/sounds/active.wav /opt/RRFScanner/status.wav
		set -- 'stop'
	else
        cp /opt/RRFScanner/sounds/desactive.wav /opt/RRFScanner/status.wav
		set -- 'start'
	fi
fi

case "$1" in
    start)
        echo "Starting RRFScanner"
        nohup python $PATH_SCRIPT --room RRF --sleep 5  --debug False > $PATH_LOG/RRFScanner.log 2>&1 & echo $! > $PATH_PID/RRFScanner.pid
        ;;
    stop) 
        echo "Stopping RRFScanner"
        kill `cat $PATH_PID/RRFScanner.pid`
        ;;
    esac