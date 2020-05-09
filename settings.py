#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
RRFRaptor
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

# Version

version = '1.4.2'

# Variables par defaut

sleep = 1                       # Durée en minutes avant QSY
scan = False                    # Mode scan
debug = False                   # Mode debug
current_room = ''               # Salon courant

active_room  = ['RRF', 'TECHNIQUE', 'LOCAL', 'BAVARDAGE', 'INTERNATIONAL']    # Liste des salons actifs (ajoutez le 'FON' si vous le souhaitez) 
passiv_room  = ['PERROQUET', 'REGIONAL', 'EXPERIMENTAL', 'FREEDV', 'NUMERIQUE', 'ECHOLINK']   # Liste des salons passifs...
active_room += passiv_room

room = {
    'RRF': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/RRF-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'rrf' 
    }, 
    'TECHNIQUE': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/TECHNIQUE-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'tec'
    }, 
    'INTERNATIONAL': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/INTERNATIONAL-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'int'
    }, 
    'LOCAL': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/LOCAL-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'loc'
    },  
    'BAVARDAGE': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/BAVARDAGE-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'bav'
    },  
    'FON': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/FON-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'fon'
    },
    'PERROQUET': {          # Salon passif
        'url': '',
        'tot': 0,
        'last': '',
        'label': 'default'
    },
    'REGIONAL': {           # Salon passif
        'url': '',
        'tot': 0,
        'last': '',
        'label': 'reg'
    },
    'EXPERIMENTAL': {       # Salon passif
        'url': '',
        'tot': 0,
        'last': '',
        'label': 'exp'
    },
    'FREEDV': {             # Salon passif
        'url': '',
        'tot': 0,
        'last': '',
        'label': 'fdv'
    },
    'NUMERIQUE': {          # Salon passif
        'url': '',
        'tot': 0,
        'last': '',
        'label': 'num'
    },
    'ECHOLINK': {           # Salon passif
        'url': '',
        'tot': 0,
        'last': '',
        'label': 'el'
    }
}