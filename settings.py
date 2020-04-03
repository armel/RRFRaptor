#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
RRFRaptor
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

# Version

version = '1.3.4'

# Variables par defaut

sleep = 1                       # Durée en minutes avant QSY
scan = False                    # Mode scan
debug = False                   # Mode debug
current_room = ''               # Salon courant

valid_room = ['PERROQUET', 'REGIONAL', 'RRF', 'TECHNIQUE', 'LOCAL', 'BAVARDAGE', 'INTERNATIONAL']    # Ajoutez le 'FON' si vous le souhaitez 

room = {
    'PERROQUET': {          # Salon passif
        'url': '',
        'tot': 0,
        'last': ''
    },
    'REGIONAL': {           # Salon passif
        'url': '',
        'tot': 0,
        'last': ''
    },
    'RRF': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/RRF-today/rrf_tiny.json',
        'tot': 0,
        'last': ''
    }, 
    'TECHNIQUE': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/TECHNIQUE-today/rrf_tiny.json',
        'tot': 0,
        'last': ''
    }, 
    'INTERNATIONAL': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/INTERNATIONAL-today/rrf_tiny.json',
        'tot': 0,
        'last': ''
    }, 
    'LOCAL': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/LOCAL-today/rrf_tiny.json',
        'tot': 0,
        'last': ''
    },  
    'BAVARDAGE': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/BAVARDAGE-today/rrf_tiny.json',
        'tot': 0,
        'last': ''
    },  
    'FON': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/FON-today/rrf_tiny.json',
        'tot': 0,
        'last': ''
    }
}