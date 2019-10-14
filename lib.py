#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
RRFScanner
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

import settings as s
import requests
import os
import time
import datetime
import json

# Usage
def usage():
    print 'Usage: RRFSentinel.py [options ...]'
    print
    print '--help                           cet aide'
    print
    print 'Parametrages:'
    print 
    print '  --sleep            nombre      Nombre de minutes avant scanning (5 minutes par défaut)'
    print '  --room             string      Salon de démarrage [RRF (défaut), TECHNIQUE, LOCAL, BAVARDAGE, INTERNATIONAL ou FON]'
    print '  --debug            booléen     Mode debug [True, False (défaut)]'
    print
    print '88 & 73 from F4HWN Armel'


# Lecture du flux Json
def read_log():

    try:
        r = requests.get(s.room[s.current_room]['url'], verify=False, timeout=10)
    except requests.exceptions.ConnectionError as errc:
        print ('Error Connecting:', errc)
    except requests.exceptions.Timeout as errt:
        print ('Timeout Error:', errt)

    rrf_data = ''
    try:
        rrf_data = r.json()
    except:
        pass

    if rrf_data != '':
        current_indicatif = rrf_data['transmit'][0]['Indicatif'].encode('utf-8')

        s.room[s.current_room]['indicatif'] = current_indicatif
        if current_indicatif != '':
            s.room[s.current_room]['last'] = time.time()
        
        for data in rrf_data['elsewhere'][1]:
            if data in s.valid_room:
                tmp = rrf_data['elsewhere'][1][data].encode('utf-8')
                if tmp != 'Aucune émission':
                    s.room[data]['indicatif'] = tmp
                else:
                    s.room[data]['indicatif'] = ''
    else:
        if s.debug is True:
            print 'Failed to read...'

    return True

# Gestion des QSY
def qsy(new_room = ''):
    cmd = ''
    old_room = s.current_room
    if new_room != '':
        cmd = '/etc/spotnik/restart.' + new_room[:3].lower()
    else:
        for data in s.valid_room:
            if data != s.current_room:
                if s.room[data]['indicatif'] != '':
                    s.current_room = data
                    s.room[s.current_room]['last'] = time.time()
                    cmd = '/etc/spotnik/restart.' + data[:3].lower()
                    break

    if cmd != '':
        now = datetime.datetime.now()
        print now.strftime('%H:%M:%S'), '- Execute', cmd, '(', old_room, ' -> ', s.current_room, ')'
        if s.debug is False:
            os.system(cmd)
            time.sleep(5)   # Petite temporisation avant de killer le timersalon éventuel
            cmd = '/usr/bin/pkill -f timersalon'
            os.system(cmd)

    return True

# Trace debugage
def trace():

    for data in s.room:
        print data, 
        if s.room[data]['indicatif'] == '':
            print s.room[data]['last']
        else:
            print s.room[data]['indicatif']
    print '-----'

    return True