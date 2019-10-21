#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
RRFRaptor
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
        options, remainder = getopt.getopt(argv, '', ['help', 'version', 'sleep=', 'scan=', 'debug='])
    except getopt.GetoptError:
        l.usage()
        sys.exit(2)
    for opt, arg in options:
        if opt == '--help':
            l.usage()
            sys.exit()
        elif opt == '--version':
            print s.version
            sys.exit()
        elif opt in ('--sleep'):
            s.sleep = float(arg)
        elif opt in ('--scan'):
            if arg in ['True', 'true']:
                s.scan = True
            else:
                s.scan = False
        elif opt in ('--debug'):
            if arg in ['True', 'true']:
                s.debug = True
            else:
                s.debug = False

    if s.scan is True: # Si scan simple
        l.where_is()
        while(True):
            if l.read_log() is True:
                file = open('/tmp/RRFRaptor_scan.tcl', 'w')
                file.write('set RRFRaptor "' + l.scan() + '"\n')
                file.close()
                sys.exit()

    else: # Sinon, boucle principale
        while(True):
            # Lecture du salon courant
            l.where_is()
            now = datetime.datetime.now()

            if s.current_room != 'PARROT':  # Si pas sur le perroquet
                # Lecture de l'activité
                l.read_log()

                # Gestion de la temporisation
                s1 = s.room[s.current_room]['last']
                s2 = time.time()

                if (s2 - s1) > s.sleep * 60: # Si la limite de temporisation atteinte, on scan
                    if s.debug is True or s.scan is True: # Attention, on réutilise ici la variable s.scan mais ne pas la confondre avec l'option --scan
                        s.scan = False
                        print now.strftime('%H:%M:%S'), '-', 'Scan en cours...'
                    l.qsy()
                else: # Sinon, on affiche éventuellement une trace
                    s.scan = True # Attention, on réutilise ici la variable s.scan mais ne pas la confondre avec l'option --scan
                    if s.debug is True:
                        print now.strftime('%H:%M:%S'), '-', 'Standby sur ' + s.current_room + ' depuis ' + str(int(s2 - s1)) + ' secondes'
            else: # Sinon on ne fait rien sur le perroquet
                if s.debug is True:
                    print now.strftime('%H:%M:%S'), '-', 'Perroquet...'

            # On controle toutes les 2 secondes, c'est suffisant...
            time.sleep(5)
            sys.stdout.flush()

if __name__ == '__main__':
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass
