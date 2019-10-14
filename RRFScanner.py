#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
RRFScanner
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

import settings as s
import lib as l

import getopt
import sys
import time
import os

def main(argv):

    # Check and get arguments
    try:
        options, remainder = getopt.getopt(argv, '', ['help', 'sleep=', 'standby='])
    except getopt.GetoptError:
        l.usage()
        sys.exit(2)
    for opt, arg in options:
        if opt == '--help':
            l.usage()
            sys.exit()
        elif opt in ('--sleep'):
            s.sleep = int(arg)
        elif opt in ('--standby'):
            s.standby_room = arg

    s.current_room = s.standby_room
    cmd = '/etc/spotnik/restart.' + s.current_room[:3].lower()
    os.system(cmd)

    if s.room[s.current_room]['last'] == '':
        s.room[s.current_room]['last'] = time.time()

    while(True):
        s1 = s.room[s.current_room]['last']
        s2 = time.time()

        #print 'Standby sur ' + s.current_room + ' depuis ' + str(int(s2 - s1)) + ' secondes'

        if (s2 - s1) > s.sleep * 60:
            #print 'Début du scan...'
            l.read_log()
            if s.room[s.current_room]['indicatif'] == '':
                l.qsy()
        
        time.sleep(2)
        sys.stdout.flush()

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
