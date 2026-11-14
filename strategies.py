import random

# Une strategie = une fonction-> "C" ou "D"

def all_d(mes_coups, ses_coups):
    return "D"

def tit_for_tat(mes_coups, ses_coups):
    if not ses_coups:          
        return "C"
    return ses_coups[-1]

def random_cd(mes_coups, ses_coups):
    return "C" if random.random() < 0.5 else "D"

def tester(mes_coups, ses_coups):
    tour = len(mes_coups)
    if tour == 0:
        return "D"
    if "D" in ses_coups:           
        return ses_coups[-1]
    #sinon je repete C,C,D!!
    return "D" if tour % 3 == 0 else "C"

def joss(mes_coups, ses_coups):
    coup = tit_for_tat(mes_coups, ses_coups)
    if coup == "C" and random.random() < 0.1:   
        return "D"
    return coup