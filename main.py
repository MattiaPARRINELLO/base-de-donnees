"""
Jeu de combat au tour par tour, joué en console.
Les scores sont enregistrés dans MongoDB via le module bdd.
"""

import jeu

if __name__ == "__main__":
    try:
        jeu.lancer_jeu()
    except KeyboardInterrupt:
        print("À bientôt")
