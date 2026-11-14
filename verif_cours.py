"""Verifie le moteur avec les chiffres des diapos du cours."""
from moteur import jouer_partie, tournoi, afficher_classement
from strategies import all_d, tit_for_tat

#diapo 67: TFT contre ALL-D sur 10 tours
score_tft, score_alld = jouer_partie(tit_for_tat, all_d, tours=10)
print("TFT contre ALL-D sur 10 tours :", score_tft, "-", score_alld, "(cours : 18 - 23)")

#diapo 68: mini-tournoi, deux TFT et un ALL-D, 1 partie de 10 tours
print("\nMini-tournoi 2 TFT + 1 ALL-D (cours : 48, 48, 46)")
joueurs = [("TFT1", tit_for_tat), ("TFT2", tit_for_tat), ("ALL-D", all_d)]
afficher_classement(tournoi(joueurs, parties=1, tours=10))

#question de la diapo 69: et avec un seul TFT et deux ALL-D ?
print("\nMini-tournoi 1 TFT + 2 ALL-D (question de la diapo 69)")
joueurs = [("TFT", tit_for_tat), ("ALL-D1", all_d), ("ALL-D2", all_d)]
afficher_classement(tournoi(joueurs, parties=1, tours=10))