"""Verifie le moteur avec les chiffres des diapos du cours."""
from moteur import jouer_partie
from strategies import all_d, tit_for_tat

#diapo 67: TFT contre ALL-D sur 10 tours
score_tft, score_alld = jouer_partie(tit_for_tat, all_d, tours=10)
print("TFT contre ALL-D sur 10 tours :", score_tft, "-", score_alld, "(cours : 18 - 23)")