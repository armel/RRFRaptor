# RRFScanner
Le RRFScanner analyse le trafic sur le réseau [RRF](https://f5nlg.wordpress.com/2015/12/28/nouveau-reseau-french-repeater-network/) (Réseau des Répéteurs Francophones) et gère automatiquement les QSY de votre Spotnik afin de lui faire rejoindre automatiquement le salon sur lequel il y a de l'activité.

# Principe de fonctionnement
Une fois le RRFScanner lancé, tant qu'il y a de l'activité sur le salon sur lequel vous êtes, il reste en sommeil.

Si l'activité retombe, au bout d'une certaine temporisation paramétrable, le RRFScanner va s'activer et commencer à analyser le trafic sur l'ensemble du réseau RRF à la recherche de QSO sur les autres salons.

Si le trafic reprend entre temps sur le salon sur lequel vous étiez, évidement, la temporisation redémarre à zéro et le RRFScanner retombe en sommeil.

Par contre, si le trafic ne reprend pas et que le RRFScanner détecte de l'activité sur un autre salon, alors il va automatiquement faire basculer votre Spotnik sur celui ci.

# Installation

## Installation du RRFScanner

En partant de la version 2 ou 3 de la distribution Spotnik, commencez par cloner ce projet dans le répertoire `/opt`. Donc, depuis une connexion SSH, lancez les commandes suivantes:

`cd /opt`

Puis, 

`git clone https://github.com/armel/RRFScanner.git`

Il faut également procéder à l'installation de quelques paquets complémentaires. Toujours depuis une connexion SSH, lancez les commandes suivantes:

`sudo apt-get install python-pip`

`sudo pip install requests`

Et voilà, c'est tout ;)

## Lancement du RRFScanner

Le plus simple est de lancer le RRFScanner en CLI (ligne de commande). Toujours depuis une connexion SSH, 

- pour activer le RRFScanner : `/opt/RRFScanner/RRFScanner.sh start`
- pour désactiver le RRFScanner : `/opt/RRFScanner/RRFScanner.sh stop`

Le RRFScanner basculera sur sa position initiale (par défaut le salon RRF). En l'absence d'activité, au bout de 1 minute (par défaut), le RRFScanner va s'activer et commencer à analyser le trafic sur l'ensemble du réseau RRF à la recherche de QSO sur les autres salons.

# Paramétrages fins

## Changer les paramétrages par défaut

Vous pouvez évidement éditer le fichier `/opt/RRFScanner/RRFScanner.sh` afin de changer le salon de départ (option `--room`) et la durée de la temporisation (option `--sleep`). 

L'option `--debug` présente juste un intérêt en phase de dévelopement. Inutile de l'activer. 

## Ne pas prendre en compte certains salons

Vous pouvez éditer le fichier `/opt/RRFScanner/settings.py` et modifier la variable `valid_room` (ligne 20) avec la liste des salons que vous voulez surveiller.


## Activation et désactivation par commande DTMF

Il est possible d'activer et de désactiver le RRFScanner par une simple commande DTMF.

Pour cela, éditez le fichier `/usr/share/svxlink/events.d/local/Logic.tcl`. Vers les lignes 600, vous trouverez des blocs de code concernant les commandes DTMF que vous connaissez déjà. Ajouter à la suite un nouveau bloc avec le code ci dessous:

```
  # 200
  if {$cmd == "200"} {
    puts "Executing external command"
    playFile /opt/RRFScanner/status.wav
    exec nohup /opt/RRFScanner/RRFScanner.sh &
    return 1
  }
```

Et voilà, le RRFScanner peut être activé ou désactivé en envoyant la commande DTMF `200`. Vous pouvez évidement choisir une autre commande.
