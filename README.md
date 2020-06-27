# RRFRaptor
Le RRFRaptor analyse le trafic sur le réseau [RRF](https://f5nlg.wordpress.com/2015/12/28/nouveau-reseau-french-repeater-network/) (Réseau des Répéteurs Francophones) et gère automatiquement les QSY de votre Spotnik afin de lui faire rejoindre automatiquement le salon sur lequel il y a de l'activité.  Attention, __il n'est pas recommandé de l'installer sur un relais__ en permanence. Par contre, il est parfaitement adapté à un usage personnel. 

> Pour ma part, j'active néanmoins le RRFRaptor sur le F1ZPX situé en JN18du, entre 22h05 et 06h05, période généralement assez calme sur le RRF. J'ai ajouté les lignes suivantes dans la crontab :

> ```
> 05 22 * * * /opt/RRFRaptor/RRFRaptor.sh start
> 05 06 * * * /opt/RRFRaptor/RRFRaptor.sh stop
> 06 06 * * * /bin/echo "96#" > /tmp/dtmf_uhf
> ```

# Principe de fonctionnement
Une fois le RRFRaptor lancé, tant qu'il y a de l'activité sur le salon sur lequel vous êtes, rien ne se passe. Le RRFRaptor reste en sommeil.

Si l'activité retombe, au bout d'une certaine temporisation paramétrable, le RRFRaptor va s'activer et commencer à analyser le trafic sur l'ensemble du réseau RRF à la recherche de QSO sur les autres salons.

Si le trafic reprend entre temps sur le salon sur lequel vous étiez, évidemment, la temporisation redémarre à zéro et le RRFRaptor retombe en sommeil.

Par contre, si le trafic ne reprend pas et que le RRFRaptor détecte de l'activité sur un autre salon, alors il va automatiquement faire basculer votre Spotnik sur celui ci.

> Par défaut, le FON n'est pas pris en charge. Mais vous pouvez l'ajouter à la liste des salons à surveiller. Voir ligne 21 du fichier `settings.py`.

# Installation

## Installation du RRFRaptor

Commencez par ouvrir une connexion SSH sur votre Spotnik.

### Etape 1 - Récupération du code

Depuis votre connexion SSH, lancez les commandes suivantes :

`cd /opt`

Puis, 

`git clone https://github.com/armel/RRFRaptor.git`

### Etape 2 - Installation des dépendances

Si nécessaire, il faut également procéder à l'installation de quelques paquets complémentaires. Rassurez-vous, ce sera rapide. Toujours depuis votre connexion SSH, lancez la commande suivante :

`sudo pip3 install requests`

### Etape 3 - Ajout des codes DTMF

Il est possible d'activer et de désactiver le RRFRaptor par un simple code DTMF.

Si vous n'êtes pas familier avec les fichiers de paramétrages de __SvxLink__, il vous suffit de copier le fichier `Logic.tcl` que j'ai déjà modifié pour vous. Donc, depuis votre connexion SSH, lancer les commandes suivantes :

`mv /usr/share/svxlink/events.d/local/Logic.tcl /usr/share/svxlink/events.d/local/Logic.tcl.bak`


`cp /opt/RRFRaptor/Logic.tcl /usr/share/svxlink/events.d/local/Logic.tcl`

La première va faire une sauvegarde de votre fichier `Logic.tcl` (renommé en `Logic.tcl.bak` au cas ou). Et la seconde va copier le fichier `Logic.tcl` modifié afin de prendre en charge le RRFRaptor. 

Le RRFRaptor pourra désormais être activé ou désactivé en envoyant le code DTMF __200__.

### Etape 4 - Redémarrage de SvxLink

Enfin, pour finir, redémarrez __SvxLink__ à l'aide de la commande suivante :

`/etc/spotnik/restart`

Et voilà, c'est tout ;) Vous êtes pret à utiliser le RRFRaptor !

## Lancement du RRFRaptor

Le plus simple est de lancer le RRFRaptor en CLI (ligne de commande). Toujours depuis une connexion SSH, 

- pour activer le RRFRaptor : `/opt/RRFRaptor/RRFRaptor.sh start`
- pour désactiver le RRFRaptor : `/opt/RRFRaptor/RRFRaptor.sh stop`

Sinon, vous pouvez également activer ou désactiver le RRFRaptor à l'aide du code DTMF __200__. 

Dans tous les cas, une annonce vocale vous informera de l'activation ou de la désactivation du RRFRaptor. 

Une fois activé, en l'absence d'activité durant 1 minute (par défaut), le RRFRaptor va commencer à analyser le trafic sur l'ensemble du réseau RRF à la recherche de QSO sur les autres salons et gérer lui même les QSY.

## Mode scan rapide

Le RRFRaptor dispose également d'une fonctionnalité de _scan rapide_. Cela permet de savoir si un QSO est en cours sur un salon, via une annonce vocale. __Il n'est pas nécessaire que le RRFRaptor soit activé pour que cette fonctionnalité soit utilisable__. On peut donc lancer un _scan rapide_ à tous moments.

En CLI (ligne de commande), depuis une connexion SSH, lancez la commande suivante :

 `/opt/RRFRaptor/RRFRaptor.sh scan`

Sinon, vous pouvez également utiliser le code DTMF __201__.

> S'il n'est pas forcément recommandé d'activer en permanence le RRFRaptor sur un relais, cette fonctionnalité de __scan rapide__ peut s'avérer très intéressante partout.  Un seul code DTMF peut renseigner les OM sur les QSO en cours sur les autres salons. À eux, si le RRFRaptor n'est pas activé, de gérer les QSY. 

# Paramétrages fins

## Changer les paramétrages par défaut

Vous pouvez évidemment éditer le fichier `/opt/RRFRaptor/RRFRaptor.sh` afin de changer la durée de la temporisation par défaut (option `--sleep`). 

>L'option `--debug` présente juste un intérêt en phase de développement. Inutile de l'activer. 

## Ne pas prendre en compte certains salons

Vous pouvez éditer le fichier `/opt/RRFRaptor/settings.py` et modifier la variable `active_room` (ligne 22) qui liste les salons _actifs_ que vous souhaitez surveiller. Idem avec la variable `passive_room` (ligne 23) pour les salons _passifs_.

À noter qu'il existe 2 types de salons : 

- Les salons _actifs_ (ligne 22) : RRF, TECHNIQUE, LOCAL, BAVARDAGE, INTERNATIONAL et FON
- Les salons _passifs_ (ligne 23) : PERROQUET, REGIONAL, EXPERIMENTAL, FREEDV, NUMERIQUE et ECHOLINK

Seuls les salons _actifs_ font l'objet d'une surveillance par le RRFRaptor. La liste des salons _passifs_ permet uniquement d'autoriser un QSY __manuel__ (via commandes DTMF ou autres) sur ces salons, même si le RRFRaptor est enclenché. Dans ce cas, le `timersalon.sh` prendra en charge le QSY avec retour sur le salon RRF en l'absence d'activité pendant 6 minutes (valeur par défaut).

Enfin, retenez que si vous forcez un QSY vers un salon __non référencé__ dans la liste des salons _actifs_ ou des salons _passifs_, le RRFRaptor vous enverra vers le salon RRF (par défaut, voir points ci dessous).

## Changer le salon par défaut

Quant le RRFRaptor est activé, le link a la possibilité d'aller sur l'ensemble des salons _actifs_ et _passifs_ (voir point ci dessus). Mais si un OM force un QSY (via commande DTMF ou autres moyens) sur un salon ne faisant pas partie de ces 2 listes, le RRFRaptor vous enverra vers le salon RRF. Il est possible de modifier ce salon. 

Vous pouvez éditer le fichier `/opt/RRFRaptor/settings.py` et modifier la variable `default_room` (ligne 21) en indiquant un salon faisant partie de la listes des salons _actifs_ : RRF, TECHNIQUE, LOCAL, BAVARDAGE, INTERNATIONAL ou FON.

>
Exemple pratique. Si vous souhaitez suivre l'ensemble des salons _actifs_ mais exclure le salon RRF et autoriser l'utilisation du PERROQUET, voici la configuration permettant de le faire en choisissant le salon TECHNIQUE comme salon par défaut :

```
default_room = 'TECHNIQUE'     # Salon par defaut si le RRFRaptor est perdu...
active_room  = ['TECHNIQUE', 'LOCAL', 'BAVARDAGE', 'INTERNATIONAL', 'FON']    # Liste des salons actifs
passive_room = ['PERROQUET']   # Liste des salons passifs...
```

## Lancer le RRFRaptor au démarrage du Spotnik

Il est évidemment possible de lancer le RRFRaptor au démarrage du Spotnik. Il suffit d'éditer le fichier `/etc/rc.local` et d'y ajouter les lignes suivantes, juste __avant__ le `exit 0` qui termine le script :

```
## demarrage Raptor
/opt/RRFRaptor/RRFRaptor.sh start
```

## Mettre à jour la version du RRFRaptor

Depuis votre connexion SSH, lancez les commandes suivantes :

`/opt/RRFRaptor/RRFRaptor.sh stop`

`cd /opt/RRFRaptor`

`git pull`

`sudo pip3 install requests`

`/opt/RRFRaptor/RRFRaptor.sh start`

Et voilà, votre version est à jour.

## Modifier les codes DTMF par défaut

Si vous le souhaitez, vous pouvez modifier les codes DTMF par défaut et les adapter suivant vos besoins. Pour se faire, éditer le fichier `/usr/share/svxlink/events.d/local/Logic.tcl` à l'aide de votre éditeur préféré. Recherchez les blocs concernant les codes DTMF (vers les lignes 600...). Ajoutez et / ou modifiez les 4 nouveaux blocs ci dessous en les adaptant à votre convenance :

```
# 200 Raptor start and stop
  if {$cmd == "200"} {
    puts "Executing external command"
    exec nohup /opt/RRFRaptor/RRFRaptor.sh &
    return 1
  }

# 201 Raptor quick scan
  if {$cmd == "201"} {
    puts "Executing external command"
    exec /opt/RRFRaptor/RRFRaptor.sh scan
    return 1
  }

# 202 Raptor sound
  if {$cmd == "202"} {
    if { [file exists /tmp/RRFRaptor_status.tcl] } {
      source "/tmp/RRFRaptor_status.tcl"
      if {$RRFRaptor == "ON"} {
        playSilence 1500
        playFile /opt/RRFRaptor/sounds/active.wav     
      } else {
        playSilence 1500
        playFile /opt/RRFRaptor/sounds/desactive.wav
      }
    }
    return 1
  }

# 203 Raptor quick scan sound
  if {$cmd == "203"} {
    if { [file exists /tmp/RRFRaptor_scan.tcl] } {
      source "/tmp/RRFRaptor_scan.tcl"
      if {$RRFRaptor == "None"} {
        playSilence 1500
        playFile /opt/RRFRaptor/sounds/qso_ko.wav        
      } else {
        playSilence 1500
        playFile /opt/RRFRaptor/sounds/qso_ok.wav
        if {$RRFRaptor == "RRF"} {
          playFile /etc/spotnik/Srrf.wav      
        } elseif {$RRFRaptor == "FON"} {
          playFile /etc/spotnik/Sfon.wav    
        } elseif {$RRFRaptor == "TECHNIQUE"} {
          playFile /etc/spotnik/Stec.wav    
        } elseif {$RRFRaptor == "INTERNATIONAL"} {
          playFile /etc/spotnik/Sint.wav    
        } elseif {$RRFRaptor == "LOCAL"} {
          playFile /etc/spotnik/Sloc.wav    
        } elseif {$RRFRaptor == "BAVARDAGE"} {
          playFile /etc/spotnik/Sbav.wav    
        }  
      }
    }
    return 1
  }
```

>Attention, si vous modifiez également les codes __202__ et __203__ qui servent aux annonces vocales, vous devrez les modifiez également dans le script `/opt/RRFRaptor/RRFRaptor.sh`. Ce changement n'est pas recommandé.

# That's all

Bon trafic à tous, 88 & 73 de Armel F4HWN !