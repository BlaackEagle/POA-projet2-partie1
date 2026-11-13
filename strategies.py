# Une strategie = une fonction (mes_coups, ses_coups) -> "C" ou "D"

def all_d(mes_coups, ses_coups):
    return "D"

def tit_for_tat(mes_coups, ses_coups):
    if not ses_coups:          
        return "C"
    return ses_coups[-1]