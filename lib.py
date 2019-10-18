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
    print '  --sleep            nombre      Nombre de minutes avant scanning (3 minutes par défaut)'
    print '  --debug            booléen     Mode debug [True, False (défaut)]'
    print
    print '88 & 73 from F4HWN Armel'


# Lecture du flux Json
def read_log():

    # Requete HTTP vers le flux json du salon produit par le RRFTracker 
    try:
        r = requests.get(s.room[s.current_room]['url'], verify=False, timeout=10)
    except requests.exceptions.ConnectionError as errc:
        print ('Error Connecting:', errc)
    except requests.exceptions.Timeout as errt:
        print ('Timeout Error:', errt)

    # Controle de la validité du flux json
    rrf_data = ''
    try:
        rrf_data = r.json()
    except:
        pass

    if rrf_data != '': # Si le flux est valide
        # On récupère le TOT du salon en court
        current_tot = rrf_data['abstract'][0]['TOT']
        s.room[s.current_room]['tot'] = current_tot

        if current_tot != 0: # Si le TOT tourne encore
            s.room[s.current_room]['last'] = time.time()
        else: # Sinon, on commence à regarder ailleurs
            for data in rrf_data['elsewhere'][6]:
                if data in s.valid_room:
                    tmp = rrf_data['elsewhere'][6][data]
                    if tmp != 0:
                        s.room[data]['tot'] = tmp
                    else:
                        s.room[data]['tot'] = 0
    else: # Si le flux est invalide
        if s.debug is True:
            print 'Failed to read...'

    return True

# Gestion des QSY
def qsy(new_room = ''):
    cmd = ''
    old_room = s.current_room

    if new_room != '': # Si une room est passée en argument
        cmd = '/etc/spotnik/restart.' + new_room[:3].lower()
    else: # Sinon
        for data in s.valid_room:
            if data != s.current_room:
                if s.room[data]['tot'] >= 3:
                    s.current_room = data
                    s.room[s.current_room]['last'] = time.time()
                    cmd = '/etc/spotnik/restart.' + data[:3].lower()
                    break

    # Si une commande est en attente... on la joue !
    if cmd != '':
        now = datetime.datetime.now()
        print now.strftime('%H:%M:%S'), '- Execute', cmd, '(', old_room, ' -> ', s.current_room, ')'
        os.system(cmd)
        time.sleep(5)   # Petite temporisation avant de killer le timersalon éventuel
        cmd = '/usr/bin/pkill -f timersalon'
        os.system(cmd)

    return True

# Detection salon
def where_is():
    detect_room = ''
    with open('/etc/spotnik/network', 'r') as content_file:
        content = content_file.read()
    content = content.strip()

    if content == 'int':
        detect_room = 'INTERNATIONAL'
    elif content == 'bav':
        detect_room = 'BAVARDAGE'
    elif content == 'loc':
        detect_room = 'LOCAL'
    elif content == 'tec':
        detect_room = 'TECHNIQUE'
    else:
        detect_room = content.upper()

    # QSY sur le salon RRF si perdu...
    if detect_room not in ['RRF', 'INTERNATIONAL', 'BAVARDAGE', 'LOCAL', 'TECHNIQUE', 'FON']:
        s.current_room = 'RRF'
        qsy(s.current_room)
        s.room[s.current_room]['last'] = time.time()
    elif detect_room != s.current_room: # Si changement de salon...
        s.current_room = detect_room
        s.room[s.current_room]['last'] = time.time()
            
    return True

# Trace debugage
def trace():
    for data in s.room:
        print data, 
        if s.room[data]['tot'] == '':
            print s.room[data]['last']
        else:
            print s.room[data]['tot']
    print '-----'

    return True