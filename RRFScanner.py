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
import datetime
import os

def main(argv):

    # Check et capture des arguments
    try:
        options, remainder = getopt.getopt(argv, '', ['help', 'sleep=', 'debug='])
    except getopt.GetoptError:
        l.usage()
        sys.exit(2)
    for opt, arg in options:
        if opt == '--help':
            l.usage()
            sys.exit()
        elif opt in ('--sleep'):
            s.sleep = float(arg)
        elif opt in ('--debug'):
            if arg in ['True', 'true']:
                s.debug = True
            else:
                s.debug = False

    # Lecture du salon courant

    with open('/etc/spotnik/network', 'r') as content_file:
        content = content_file.read()

    content = content.strip()

    if content == 'int':
        s.current_room = 'INTERNATIONAL'
    elif content == 'bav':
        s.current_room = 'BAVARDAGE'
    elif content == 'loc':
        s.current_room = 'LOCAL'
    elif content == 'tec':
        s.current_room = 'TECHNIQUE'
    else:
        s.current_room = content.upper()

    # QSY sur le salon RRF si perdu...
    if s.current_room not in ['RRF', 'INTERNATIONAL', 'BAVARDAGE', 'LOCAL', 'TECHNIQUE', 'FON']:
        s.current_room = 'RRF'
        l.qsy(s.current_room)

    # Initialisation du timer
    s.room[s.current_room]['last'] = time.time()

    # Boucle principale
    while(True):
        now = datetime.datetime.now()

        s1 = s.room[s.current_room]['last']
        s2 = time.time()

        if (s2 - s1) > s.sleep * 60: # Si la limite de temporisation atteinte, on scan
            l.read_log()
            if s.room[s.current_room]['tot'] == 0:
                if s.debug is True:
                    print now.strftime('%H:%M:%S'), '-', 'Scan en cours...'
                l.qsy()
        else: # Sinon, on affiche éventuellement une trace
            if s.debug is True:
                print now.strftime('%H:%M:%S'), '-', 'Standby sur ' + s.current_room + ' depuis ' + str(int(s2 - s1)) + ' secondes'

        # On controle toutes les 2 secondes, c'est suffisant...
        time.sleep(2)
        sys.stdout.flush()

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
