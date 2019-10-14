#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
RRFSentinel
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

import settings as s
import requests
import os
import time
import json

# Usage
def usage():
    print 'Usage: RRFSentinel.py [options ...]'
    print
    print '--help                           cet aide'
    print
    print 'Parametrages:'
    print 
    print '  --sleep            nombre      nombre de minutes avant scanning'
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
            if data in s.room:
                tmp = rrf_data['elsewhere'][1][data].encode('utf-8')
                if tmp != 'Aucune émission':
                    s.room[data]['indicatif'] = tmp
                else:
                    s.room[data]['indicatif'] = ''

    return True

def qsy():
    for data in s.room:
        if data != s.current_room:
            if s.room[data]['indicatif'] != '':
                s.current_room = data
                s.room[s.current_room]['last'] = time.time()
                cmd = '/etc/spotnik/restart.' + data[:3].lower()
                os.system(cmd)
                break

# Affichage ddebug
def debug():

    for data in s.room:
        print data, 
        if s.room[data]['indicatif'] == '':
            print s.room[data]['last']
        else:
            print s.room[data]['indicatif']
    print '-----'

    return True