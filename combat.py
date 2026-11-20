import math
import time

import affichage
from constantes import PAUSE_ROUND
from predicats import est_vivant, tous_vaincus


def calculer_degats(attaquant, defenseur):
    degats = math.floor(
        attaquant["attaque"] - defenseur["defense"] / 2
    )  # Limite combat trop long ex. Gérard x Jo (130 tours sans)
    if degats < 1:
        return 1
    return degats


def attaquer(attaquant, defenseur):
    degats = calculer_degats(attaquant, defenseur)
    defenseur["hp"] -= degats
    return degats


def echanger_coups(perso, opposant):
    degats_perso = attaquer(perso, opposant)
    if not est_vivant(opposant):
        return degats_perso, 0
    degats_opposant = attaquer(opposant, perso)
    return degats_perso, degats_opposant


def duel(perso, opposant):
    # le perso frappe en premier, l'opposant ne riposte
    # que s'il est encore vivant
    while est_vivant(perso) and est_vivant(opposant):
        degats_perso, degats_opposant = echanger_coups(perso, opposant)
        affichage.afficher_round(
            perso, opposant, degats_perso, degats_opposant
        )
        time.sleep(PAUSE_ROUND)
    return est_vivant(perso)


def tour_de_combat(persos_restants, opposants_restants):
    # le gagnant du duel reste en tête avec ses HP, le perdant
    # sort de sa file : on affronte les opposants un par un
    perso = persos_restants[0]
    opposant = opposants_restants[0]
    if duel(perso, opposant):
        opposants_restants.pop(0)
    else:
        persos_restants.pop(0)


def combat_en_cours(persos_restants, opposants_restants):
    if tous_vaincus(persos_restants):
        return False
    if tous_vaincus(opposants_restants):
        return False
    return True


def combattre(equipe, liste_opposants):
    persos_restants = list(equipe)
    opposants_restants = list(liste_opposants)
    # copie superficielle : la liste est nouvelle mais les dicts sont partagés,
    # les HP perdus restent donc visibles pour compter_vaincus
    while combat_en_cours(persos_restants, opposants_restants):
        tour_de_combat(persos_restants, opposants_restants)
    if not tous_vaincus(opposants_restants):
        return False
    return True
