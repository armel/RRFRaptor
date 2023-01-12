#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
RRFRaptor
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

# Version

version = '1.5.5'

# Variables par defaut

scan_sleep = 60                 # Durée en secondes avant scanning
park = True                     # Retour sur le salon par default, en phase de scan
park_sleep = 300                # Durée en secondes avant parking

room_base = 'IDF'               # Salon de base si le RRFRaptor est perdu...
room_active  = ['RRF', 'TECHNIQUE', 'INTERNATIONAL', 'BAVARDAGE', 'LOCAL', 'EXPERIMENTAL', 'IDF']    # Liste des salons actifs
room_passive = ['PERROQUET', 'FON', 'FREEDV', 'NUMERIQUE', 'ECHOLINK', 'ADMIN']   # Liste des salons passifs...

# Autres variables (ne pas modifier si vous ne savez pas ce que vous faites...)

scan = False                    # Mode scan
debug = False                   # Mode debug
room_current = ''               # Salon courant
room_active += room_passive     # Don't tread on me ;)

room = {
    'RRF': {
        'url': 'http://rrf.globalis-dev.com:8080/RRFTracker/RRF-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'rrf' 
    }, 
    'FON': {
        'url': 'http://rrf.globalis-dev.com:8080/RRFTracker/FON-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'fon'
    },
    'TECHNIQUE': {
        'url': 'http://rrf.globalis-dev.com:8080/RRFTracker/TECHNIQUE-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'tec'
    }, 
    'INTERNATIONAL': {
        'url': 'http://rrf.globalis-dev.com:8080/RRFTracker/INTERNATIONAL-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'int'
    }, 
    'BAVARDAGE': {
        'url': 'http://rrf.globalis-dev.com:8080/RRFTracker/BAVARDAGE-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'bav'
    },  
    'LOCAL': {
        'url': 'http://rrf.globalis-dev.com:8080/RRFTracker/LOCAL-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'loc'
    }, 
    'EXPERIMENTAL': {  
        'url': 'http://rrf.globalis-dev.com:8080/RRFTracker/EXPERIMENTAL-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'exp'
    }, 
    'IDF': { 
        'url': 'http://rrf.globalis-dev.com:8080/RRFTracker/IDF-today/rrf_tiny.json',
        'tot': 0,
        'last': '',
        'label': 'idf'
    },
    'PERROQUET': {          # Salon passif
        'url': '',
        'tot': 0,
        'last': '',
        'label': 'default'
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
    },
    'ADMIN': {              # Salon passif
        'url': '',
        'tot': 0,
        'last': '',
        'label': 'admin'
    }
}