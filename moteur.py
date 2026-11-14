GAINS = {
    ("C", "C"): (3, 3),
    ("C", "D"): (0, 5),
    ("D", "C"): (5, 0),
    ("D", "D"): (2, 2),
}

def jouer_partie(strat_a, strat_b, tours=200):
    """Fait jouer une partie entre deux strategies, renvoie leurs deux scores."""
    hist_a, hist_b = [], []
    score_a, score_b = 0, 0
    for _ in range(tours):
        #les deux choisissent en meme temps 
        coup_a = strat_a(hist_a, hist_b)
        coup_b = strat_b(hist_b, hist_a)
        gain_a, gain_b = GAINS[(coup_a, coup_b)]
        score_a += gain_a
        score_b += gain_b
        hist_a.append(coup_a)
        hist_b.append(coup_b)
    return score_a, score_b 

def tournoi(joueurs, parties=5, tours=200):
    """Tous contre tous. joueurs = liste de (nom,strategie).
    Renvoie un dictionnaire {nom: score total}."""
    scores = {nom: 0 for nom, _ in joueurs}
    for i in range(len(joueurs)):
        for j in range(i + 1, len(joueurs)):   
            nom_a, strat_a = joueurs[i]
            nom_b, strat_b = joueurs[j]
            for _ in range(parties):
                score_a, score_b = jouer_partie(strat_a, strat_b, tours)
                scores[nom_a] += score_a
                scores[nom_b] += score_b
    return scores

def afficher_classement(scores):
    classement = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for rang, (nom, score) in enumerate(classement, start=1):
        print(f"{rang}. {nom:<12} {score}")

