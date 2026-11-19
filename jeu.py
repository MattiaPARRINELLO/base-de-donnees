import random

import questionary

import affichage
import bdd
import catalogue
import combat
import predicats
import saisie
from constantes import NOMBRE_OPPOSANTS, TAILLE_EQUIPE


def lancer_jeu():
    bdd.initialiser_base()
    while True:
        affichage.afficher_meilleur_score()
        choix = demander_choix_menu()
        action = options_menu()[choix]["action"]
        if action is None:
            return
        action()


def options_menu():
    return {
        1: {"nom": "Nouvelle partie", "action": demarrer_partie},
        2: {
            "nom": "Voir les personnages",
            "action": affichage.afficher_personnages,
        },
        3: {"nom": "Voir les scores", "action": affichage.afficher_scores},
        4: {"nom": "Quitter", "action": None},
    }


def demander_choix_menu():
    options = options_menu()
    choix = [
        questionary.Choice(option["nom"], value=numero)
        for numero, option in options.items()
    ]
    return saisie.demander_selection("Ton choix : ", choix)


def compter_vaincus(liste_opposants):
    vaincus = 0
    for opposant in liste_opposants:
        if not predicats.est_vivant(opposant):
            vaincus += 1
    return vaincus


def tirer_opposants():
    cles = list(catalogue.opposants.keys())
    random.shuffle(cles)
    liste = []
    for cle in cles[:NOMBRE_OPPOSANTS]:
        # même raison que pour l'équipe : on copie pour ne pas
        # abîmer les opposants du catalogue
        liste.append(
            dict(
                catalogue.opposants[cle], hp_max=catalogue.opposants[cle]["hp"]
            )
        )
    return liste


def equipe_complete(equipe):
    if len(equipe) != TAILLE_EQUIPE:
        return False
    return True


def valider_equipe(equipe):
    if equipe_complete(equipe):
        return True
    return f"Choisis exactement {TAILLE_EQUIPE} personnages"


def creer_equipe():
    choix = [
        questionary.Choice(affichage.formater_perso(perso), value=perso)
        for perso in catalogue.persos.values()
    ]
    equipe = saisie.demander_selection(
        f"Choisis tes {TAILLE_EQUIPE} personnages : ",
        choix,
        valider_equipe,
    )
    # copie pour chaque perso : sinon leurs HP baissent dans le catalogue
    return [dict(perso, hp_max=perso["hp"]) for perso in equipe]


def demarrer_partie():
    pseudo = saisie.demander_pseudo()
    equipe = creer_equipe()
    liste_opposants = tirer_opposants()
    victoire = combat.combattre(equipe, liste_opposants)
    affichage.afficher_resultat(victoire)
    enregistrer_partie(pseudo, victoire, liste_opposants)


def enregistrer_partie(pseudo, victoire, liste_opposants):
    vaincus = compter_vaincus(liste_opposants)
    bdd.enregistrer_score(pseudo, victoire, vaincus)
    print(f"Score enregistré : {vaincus} opposant(s) vaincu(s)")
