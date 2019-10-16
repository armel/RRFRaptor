#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
RRFScanner
Learn more about RRF on https://f5nlg.wordpress.com
73 & 88 de F4HWN Armel
'''

# Version

version = '1.0.3'

# Variables par defaut

sleep = 3                       # Durée en minutes avant QSY
debug = False                   # Mode debug
current_room = 'RRF'            # Salon de depart

valid_room = ['RRF', 'TECHNIQUE', 'LOCAL', 'BAVARDAGE', 'INTERNATIONAL']    # Ajoutez le 'FON' si vous le souhaitez 

room = {
    'RRF': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/RRF-today/rrf.json',
        'tot': 0,
        'last': ''
    }, 
    'TECHNIQUE': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/TECHNIQUE-today/rrf.json',
        'tot': 0,
        'last': ''
    }, 
    'INTERNATIONAL': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/INTERNATIONAL-today/rrf.json',
        'tot': 0,
        'last': ''
    }, 
    'LOCAL': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/LOCAL-today/rrf.json',
        'tot': 0,
        'last': ''
    },  
    'BAVARDAGE': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/BAVARDAGE-today/rrf.json',
        'tot': 0,
        'last': ''
    },  
    'FON': {
        'url': 'http://rrf.f5nlg.ovh:8080/RRFTracker/FON-today/rrf.json',
        'tot': 0,
        'last': ''
    }
}