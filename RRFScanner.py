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

    # Boucle principale
    while(True):
        # Lecture du salon courant
        l.where_is()

        # Gestion de la temporisation
        now = datetime.datetime.now()
        l.read_log()

        s1 = s.room[s.current_room]['last']
        s2 = time.time()

        if (s2 - s1) > s.sleep * 60: # Si la limite de temporisation atteinte, on scan
            if s.debug is True:
                print now.strftime('%H:%M:%S'), '-', 'Scan en cours...'
            l.qsy()
        else: # Sinon, on affiche éventuellement une trace
            if s.debug is True:
                print now.strftime('%H:%M:%S'), '-', 'Standby sur ' + s.current_room + ' depuis ' + str(int(s2 - s1)) + ' secondes'

        # On controle toutes les 2 secondes, c'est suffisant...
        time.sleep(5)
        sys.stdout.flush()

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
