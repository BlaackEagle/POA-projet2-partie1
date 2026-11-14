"""
python main.py etape1
"""
import random
import sys

from moteur import tournoi, afficher_classement
from strategies import all_d, random_cd, tit_for_tat, tester, joss

GRAINE = 42

COURS = [
    ("ALL-D", all_d),
    ("RANDOM", random_cd),
    ("TIT-FOR-TAT", tit_for_tat),
    ("TESTER", tester),
    ("JOSS", joss),
]

def etape1():
    print("Etape 1 : les 5 strategies du cours, 5 parties de 200 tours")
    afficher_classement(tournoi(COURS))

if __name__ == "__main__":
    random.seed(GRAINE)
    if len(sys.argv) == 2 and sys.argv[1] == "etape1":
        etape1()
    else:
        print(__doc__.strip())