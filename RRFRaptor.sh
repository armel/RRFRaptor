#!/bin/sh

PATH_SCRIPT='/opt/RRFRaptor/RRFRaptor.py'
PATH_LOG='/tmp'
PATH_PID='/tmp'

# Si pas d'argument, on gere tout seul
if [ -z "$1" ]; then
    /usr/bin/pgrep -f 'python3 /opt/RRFRaptor/RRFRaptor.py'
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
        search="python3 ${PATH_SCRIPT}"
        pkill -f "${search}"
        nohup python3 $PATH_SCRIPT --scan False --debug False > $PATH_LOG/RRFRaptor.log 2>&1 &
        echo 'set RRFRaptor "ON"' > /tmp/RRFRaptor_status.tcl
        echo "202#"> /tmp/dtmf_uhf
        echo "202#"> /tmp/dtmf_vhf
        ;;
    stop) 
        echo "Stopping RRFRaptor"
        search="python3 ${PATH_SCRIPT}"
        pkill -f "${search}"
        echo 'set RRFRaptor "OFF"' > /tmp/RRFRaptor_status.tcl
        echo "202#"> /tmp/dtmf_uhf
        echo "202#"> /tmp/dtmf_vhf
        ;;
    scan)
        echo "Simple Scan RRFRaptor"
        python3 $PATH_SCRIPT --scan True --debug False
        echo "203#"> /tmp/dtmf_uhf
        echo "203#"> /tmp/dtmf_vhf
        ;;
    version)
        echo "Version RRFRaptor"
        python3 $PATH_SCRIPT --version
        ;;
    esac