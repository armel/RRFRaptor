#!/bin/sh

PATH_SCRIPT='/opt/RRFRaptor/RRFRaptor.py'
PATH_LOG='/tmp'
PATH_PID='/tmp'

# Si pas d'argument, on gere tout seul
if [ -z "$1" ]; then
    /usr/bin/pgrep -f 'python /opt/RRFRaptor/RRFRaptor.py'
    pid=$?
    if [ $pid != 1 ]; then
        set -- 'stop'
    else
        set -- 'start'
    fi
fi

case "$1" in
    start)
        echo "Starting RRFRaptor"
        pkill -f 'python ${PATH_SCRIPT}'
        nohup python $PATH_SCRIPT --sleep 1  --debug False > $PATH_LOG/RRFRaptor.log 2>&1 & echo $! > $PATH_PID/RRFRaptor.pid
        echo "201#"> /tmp/dtmf_uhf
        echo "201#"> /tmp/dtmf_vhf
        ;;
    stop) 
        echo "Stopping RRFRaptor"
        kill `cat $PATH_PID/RRFRaptor.pid`
        echo "202#"> /tmp/dtmf_uhf
        echo "202#"> /tmp/dtmf_vhf
        ;;
    esac