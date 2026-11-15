"""
python main.py etape1
"""
import random
import sys

from moteur import tournoi, afficher_classement, afficher_duels
from strategies import all_d, random_cd, tit_for_tat, tester, joss

GRAINE = 42

COURS = [
    ("ALL-D", all_d),
    ("RANDOM", random_cd),
    ("TIT-FOR-TAT", tit_for_tat),
    ("TESTER", tester),
    ("JOSS", joss),
]

PARTIES = 5
TOURS = 200

def lancer(titre, joueurs):
    print(titre)
    duels = {}
    afficher_classement(tournoi(joueurs, PARTIES, TOURS, duels))
    print("\nPoints moyens par tour:")
    afficher_duels(joueurs, duels, PARTIES * TOURS)

def etape1():
    lancer("Etape 1 : les 5 strategies du cours, 5 parties de 200 tours", COURS)

if __name__ == "__main__":
    random.seed(GRAINE)
    if len(sys.argv) == 2 and sys.argv[1] == "etape1":
        etape1()
    else:
        print(__doc__.strip())