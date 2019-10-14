# RRFScanner
Le RRFScanner analyse le trafic sur le réseau RRF et gère automatiquement les QSY de votre Spotnik afin de lui faire rejoindre automatiquement le salon sur lequel il y a de l'activité.

# Principe de fonctionnement
Une fois le RRFScanner lancé, tant qu'il y a de l'activité sur le salon sur lequel vous êtes, le RRFScanner reste en sommeil.

Si l'activité retombe, au bout d'une certaine temporisation paramétrable, le RRFScanner va s'activer et commencer à analyser le trafic sur l'ensemble du réseau RRF à la recherche de QSO sur les autres salons.

Si le trafic reprend sur le salon sur lequel vous étiez, évidement, la temporisation redémarre à zéro et le RRFScanner retombe en sommeil.

Par contre, si le trafic ne reprend pas et que le RRFScanner détecte de l'activité sur un autre salon, alors il va automatiquement faire basculer votre Spotnik sur celui ci.

# Installation

## Installation du RRFScanner

En partant de la version 2 ou 3 de la distribution Spotnik, commencez par cloner ce projet dans le répertoire `/opt`. Donc, depuis une connexion SSH, lancez les commandes suivantes:

`cd /opt`

Puis, 

`git clone https://github.com/armel/RRFScanner.git`

Il faut également procéder à l'installation de quelques paquets complémentaires. Toujours depuis une connexion SSH, lancez les commandes suivantes:

`sudo apt-get apt-get install python-pip`

`sudo pip install requests`

Et voilà, c'est tout ;)

## Lancement du RRFScanner

Todo