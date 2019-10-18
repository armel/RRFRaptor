#!/bin/sh

PATH_SCRIPT='/opt/RRFScanner/RRFScanner.py'
PATH_LOG='/tmp'
PATH_PID='/tmp'

# Si pas d'argument, on gere tout seul
if [ -z "$1" ]; then
	/usr/bin/pgrep -f 'python /opt/RRFScanner/RRFScanner.py'
	pid=$?
	if [ $pid != 1 ]; then
		set -- 'stop'
        rm /tmp/status.wav
        ln -s /opt/RRFScanner/sounds/desactive.wav /tmp/status.wav
	else
		set -- 'start'
        rm /tmp/status.wav
        ln -s /opt/RRFScanner/sounds/active.wav /tmp/status.wav
	fi
fi

sleep 2

case "$1" in
    start)
        echo "Starting RRFScanner"
        nohup python $PATH_SCRIPT --sleep 1  --debug False > $PATH_LOG/RRFScanner.log 2>&1 & echo $! > $PATH_PID/RRFScanner.pid
        ;;
    stop) 
        echo "Stopping RRFScanner"
        kill `cat $PATH_PID/RRFScanner.pid`
        ;;
    esac