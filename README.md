# Tournoi du dilemme du prisonnier itéré

KABOURI OUZENNOU Jaouad — HAI716, projet 2 partie 1

Python 3, sans bibliothèque à installer. Tout se lance depuis la racine du dépôt.

Les commandes pour relancer chaque tournoi:

 Commande | Ce que ça lance |
|---|---|
| `python verif_cours.py` | vérification du moteur avec les diapos 67, 68 et 69 |
| `python main.py etape1` | étape 1 : les 5 stratégies du cours, format d'Axelrod |
| `python main.py etape2` | étape 2 : les 5 du cours + VENGEUR et TF2T |
| `python main.py gains` | étape 3 : autres gains, D/D vaut 1 au lieu de 2 |
| `python main.py bruit` | étape 3 : bruit, chaque coup inversé avec 5 % de chances |

Chaque tournoi affiche le classement et les points moyens par tour de chaque duel. La graine aléatoire est fixée, donc les résultats sont les mêmes à chaque lancement.
