#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
RRFRaptor
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

import settings as s
import requests
import os
import time
import datetime
import json
import sys

# Usage
def usage():
    print('Usage: RRFRaptor.py [options ...]')
    print()
    print('--help                           Cet aide')
    print('--version                        Numéro de version')
    print()
    print('Parametrages:')
    print() 
    print('  --scan_sleep       nombre      Nombre de secondes avant scanning (60 secondes par défaut)')
    print('  --park             booléen     Mode parking [True, False (défaut)]')
    print('  --park_sleep       nombre      Nombre de secondes avant parking (60 secondes par défaut)')
    print('  --scan             booléen     Mode scan [True, False (défaut)]')
    print('  --debug            booléen     Mode debug [True, False (défaut)]')
    print()
    print('88 & 73 from F4HWN Armel')


# Lecture du flux Json
def read_log():

    # Requete HTTP vers le flux json du salon produit par le RRFTracker 
    try:
        r = requests.get(s.room[s.room_current]['url'], verify=False, timeout=10)
    except requests.exceptions.ConnectionError as errc:
        print(('Error Connecting:', errc))
    except requests.exceptions.Timeout as errt:
        print(('Timeout Error:', errt))

    # Controle de la validité du flux json
    rrf_data = ''
    try:
        rrf_data = r.json()
    except:
        pass

    if rrf_data != '': # Si le flux est valide
        # On récupère le TOT du salon en court
        tot_current = rrf_data['abstract'][0]['TOT']
        s.room[s.room_current]['tot'] = tot_current

        if tot_current != 0: # Si le TOT tourne encore
            s.room[s.room_current]['last'] = time.time()
        else: # Sinon, on commence à regarder ailleurs
            try:
                for data in rrf_data['elsewhere'][6]:
                    if data in s.room_active and data not in s.room_passive:
                        tmp = rrf_data['elsewhere'][6][data]
                        if tmp != 0:
                            s.room[data]['tot'] = tmp
                        else:
                            s.room[data]['tot'] = 0
            except:
                if s.debug is True:
                    print('KeyError: \'elsewhere\'')
                return False
    else: # Si le flux est invalide
        if s.debug is True:
            print('Failed to read...')
        return False

    return True

# Gestion des QSY
def qsy(room_new = ''):
    cmd = ''
    room_old = s.room_current

    if room_new != '': # Si une room est passée en argument
        cmd = '/etc/spotnik/restart.' + room_new[:3].lower()
    else: # Sinon
        for data in s.room_active:
            if data != s.room_current:
                if s.room[data]['tot'] >= 3:
                    s.room_current = data
                    s.room[s.room_current]['last'] = time.time()
                    cmd = '/etc/spotnik/restart.' + data[:3].lower()
                    break

    # Si une commande est en attente... on la joue !
    if cmd != '':
        now = datetime.datetime.now()
        print(now.strftime('%H:%M:%S') + ' - Execute ' + cmd + ' (' + room_old + ' -> ' + s.room_current + ')')
        sys.stdout.flush()
        os.system(cmd)
        time.sleep(5)   # Petite temporisation avant de killer le timersalon éventuel
        cmd = '/usr/bin/pkill -f timersalon'
        os.system(cmd)

    return True

# Gestion du scan simple
def scan():
    for data in s.room_active:
        if s.room[data]['tot'] >= 3:
            return data
            break
    return 'None'

# Detection salon
def where_is():
    room_detect = ''
    with open('/etc/spotnik/network', 'r') as content_file:
        content = content_file.read()
    content = content.strip()

    for r in s.room:
        if s.room[r]['label'] == content:
            room_detect = r

    # QSY sur le salon par defaut si perdu...
    if room_detect not in s.room_active:
        s.room_current = s.room_base
        qsy(s.room_current)
        s.room[s.room_current]['last'] = time.time()
    elif room_detect != s.room_current: # Si changement de salon...
        if s.scan is False:
            now = datetime.datetime.now()
            print(now.strftime('%H:%M:%S') + ' - QSY manuel (' + s.room_current + ' -> ' + room_detect + ')')
            sys.stdout.flush()
        s.room_current = room_detect
        s.room[s.room_current]['last'] = time.time()
            
    return True
