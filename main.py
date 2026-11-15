"""
python main.py etape1
python main.py etape2
"""
import random
import sys

from moteur import GAINS, tournoi, afficher_classement, afficher_duels
from strategies import all_d, random_cd, tit_for_tat, tester, joss, vengeur, tit_for_two_tats

GRAINE = 42

COURS = [
    ("ALL-D", all_d),
    ("RANDOM", random_cd),
    ("TIT-FOR-TAT", tit_for_tat),
    ("TESTER", tester),
    ("JOSS", joss),
]
ETAPE2 = COURS + [
    ("VENGEUR", vengeur),
    ("TF2T", tit_for_two_tats),
]

PARTIES = 5
TOURS = 200

#etape 3 (autres gains): D/D rapporte 1 au lieu de 2
GAINS_DD1 = dict(GAINS)
GAINS_DD1[("D", "D")] = (1, 1)

def lancer(titre, joueurs, gains=GAINS):
    print(titre)
    duels = {}
    afficher_classement(tournoi(joueurs, PARTIES, TOURS, duels, gains))
    print("\nPoints moyens par tour:")
    afficher_duels(joueurs, duels, PARTIES * TOURS)

def etape1():
    lancer("Etape 1 : les 5 strategies du cours, 5 parties de 200 tours", COURS)

def etape2():
    lancer("Etape 2 : les 5 du cours + les 2 nouvelles", ETAPE2)

def etape3_gains():
    lancer("Etape 3, autres gains : D/D = 1 au lieu de 2", ETAPE2, GAINS_DD1)

COMMANDES = {"etape1": etape1, "etape2": etape2, "gains": etape3_gains}

if __name__ == "__main__":
    random.seed(GRAINE)
    if len(sys.argv) == 2 and sys.argv[1] in COMMANDES:
        COMMANDES[sys.argv[1]]()
    else:
        print(__doc__.strip())