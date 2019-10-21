#!/bin/sh

PATH_SCRIPT='/opt/RRFRaptor/RRFRaptor.py'
PATH_LOG='/tmp'
PATH_PID='/tmp'

# Si pas d'argument, on gere tout seul
if [ -z "$1" ]; then
    /usr/bin/pgrep -f 'python /opt/RRFRaptor/RRFRaptor.py'
    pid=$?
    if [ $pid != 1 ]; then
        set -- 'dtmf_stop'
        if [ -e /tmp/status.wav ]
        then
            rm /tmp/status.wav
        fi
        ln -s /opt/RRFRaptor/sounds/desactive.wav /tmp/status.wav
    else
        set -- 'dtmf_start'
        if [ -e /tmp/status.wav ]
        then
            rm /tmp/status.wav
        fi
        ln -s /opt/RRFRaptor/sounds/active.wav /tmp/status.wav
    fi
fi

sleep 2

case "$1" in
    start)
        echo "Starting RRFRaptor"
        kill `cat $PATH_PID/RRFRaptor.pid`
        echo "200#"> /tmp/dtmf_uhf
        echo "200#"> /tmp/dtmf_vhf
        ;;
    stop) 
        echo "Stopping RRFRaptor"
        echo "200#"> /tmp/dtmf_uhf
        echo "200#"> /tmp/dtmf_vhf
        ;;
    dtmf_start)
        nohup python $PATH_SCRIPT --sleep 1  --debug False > $PATH_LOG/RRFRaptor.log 2>&1 & echo $! > $PATH_PID/RRFRaptor.pid
        ;;
    dtmf_stop)
        kill `cat $PATH_PID/RRFRaptor.pid`
        ;;
    esac