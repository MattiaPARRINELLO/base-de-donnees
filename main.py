"""
Jeu de combat au tour par tour, joué en console.
Les scores sont enregistrés dans MongoDB via le module bdd.
"""

import math
import random

import questionary

import bdd

persos = {
    "gerard": {
        "nom": "Gérard",
        "hp": 120,
        "attaque": 35,
        "defense": 60,
        "arme": "une chaise pliante",
    },
    "ketty": {
        "nom": "Ketty",
        "hp": 85,
        "attaque": 70,
        "defense": 15,
        "arme": "un rouleau à pâtisserie rouillé",
    },
    "bruno": {
        "nom": "Bruno",
        "hp": 200,
        "attaque": 20,
        "defense": 85,
        "arme": "son corps, littéralement",
    },
    "sacha": {
        "nom": "Sacha",
        "hp": 60,
        "attaque": 95,
        "defense": 5,
        "arme": "des insultes très précises",
    },
}

opposants = {
    "tonton_jo": {
        "nom": "Tonton Jo",
        "hp": 130,
        "attaque": 45,
        "defense": 50,
        "arme": "son camion, en marche arrière",
    },
    "la_voisine": {
        "nom": "La Voisine",
        "hp": 90,
        "attaque": 80,
        "defense": 20,
        "arme": "un balai et beaucoup de temps libre",
    },
    "le_stagiaire": {
        "nom": "Le Stagiaire",
        "hp": 40,
        "attaque": 15,
        "defense": 10,
        "arme": "un badge qui dit AUTORISÉ",
    },
    "mireille": {
        "nom": "Mireille, 68 ans",
        "hp": 70,
        "attaque": 99,
        "defense": 30,
        "arme": "un sac à main plus lourd qu'un parpaing",
    },
}


TAILLE_EQUIPE = 3
NOMBRE_SCORES_AFFICHES = 10


def lancer_jeu():
    bdd.initialiser_base()
    while True:
        afficher_meilleur_score()
        choix = demander_choix_menu()
        action = options_menu()[choix]["action"]
        if action is None:
            return
        action()


def demander_choix_menu():
    options = options_menu()
    choix = [
        questionary.Choice(option["nom"], value=numero)
        for numero, option in options.items()
    ]
    return questionary.select("Ton choix : ", choices=choix).unsafe_ask()


def afficher_personnages():
    afficher_liste_persos(persos_disponibles([]))


def options_menu():
    return {
        1: {"nom": "Nouvelle partie", "action": demarrer_partie},
        2: {"nom": "Voir les personnages", "action": afficher_personnages},
        3: {"nom": "Voir les scores", "action": afficher_scores},
        4: {"nom": "Quitter", "action": None},
    }


def compter_vaincus(liste_opposants):
    vaincus = 0
    for opposant in liste_opposants:
        if not est_vivant(opposant):
            vaincus += 1
    return vaincus


def demarrer_partie():
    pseudo = demander_pseudo()
    equipe = creer_equipe()
    liste_opposants = tirer_opposant()
    victoire = combattre(equipe, liste_opposants)
    if victoire:
        print("Victoire")
    else:
        print("Défaite")
    vaincus = compter_vaincus(liste_opposants)
    bdd.enregistrer_score(pseudo, victoire, vaincus)
    print(f"Score enregistré : {vaincus} opposant(s) vaincu(s)")


def demander_pseudo():
    return (
        questionary.text("Entre ton pseudo : ", validate=pseudo_valide)
        .unsafe_ask()
        .strip()
    )


def pseudo_valide(pseudo):
    if len(pseudo) > 40:
        return False
    if len(pseudo) < 3:  # noqa: SIM103
        return False
    else:
        return True


def creer_equipe():
    equipe = []
    while not equipe_complete(equipe):
        equipe.append(demander_perso(equipe))
    return equipe


def equipe_complete(equipe):
    if len(equipe) >= TAILLE_EQUIPE:  # noqa: SIM103
        return True
    return False


def demander_perso(equipe):
    liste = persos_disponibles(equipe)
    choix = [questionary.Choice(formater_perso(perso), value=perso) for perso in liste]
    perso = questionary.select("Choix du personage : ", choices=choix).unsafe_ask()
    # copie du perso : sinon ses HP baissent dans le catalogue
    # et il revient blessé à la partie suivante
    return dict(perso)


def persos_disponibles(a_tronquer):
    nom_pris = []
    for perso in a_tronquer:
        nom_pris.append(perso["nom"])
    liste = []
    for perso in persos.values():
        if perso["nom"] not in nom_pris:
            liste.append(perso)
    return liste


def afficher_liste_persos(liste):
    index = 1
    for perso in liste:
        afficher_perso_formate(perso, index)
        index += 1


def formater_perso(perso):
    return f"{perso['nom']} HP: {perso['hp']} ATT: {perso['attaque']} DEF: {perso['defense']} ARME: {perso['arme']}"


def afficher_perso_formate(perso, index):
    print(f"{index}. {formater_perso(perso)}")


def afficher_scores():
    scores = bdd.lire_scores(NOMBRE_SCORES_AFFICHES)
    if len(scores) == 0:
        print("Aucun score enregistré")
        return
    index = 1
    for score in scores:
        print(
            f"{index}. {score['pseudo']} - {score['opposants_vaincus']} vaincus - {score['date_partie']:%d/%m/%Y %H:%M:%S}"
        )
        index += 1


def afficher_meilleur_score():
    score = bdd.lire_meilleur_score()
    if score is None:
        print("Aucun score enregistré")
        return
    print(f"Record : {score['pseudo']} - {score['opposants_vaincus']} vaincus")


def tirer_opposant():
    cles = list(opposants.keys())
    random.shuffle(cles)
    liste = []
    for cle in cles:
        # même raison que pour l'équipe : on copie pour ne pas abîmer les opposants du catalogue
        liste.append(dict(opposants[cle]))
    return liste


def combattre(equipe, liste_opposants):
    persos_restants = list(equipe)
    opposants_restants = list(liste_opposants)
    # copie superficielle : la liste est nouvelle mais les dicts sont partagés
    # donc les HP perdus pendant le combat restent visibles pour compter_vaincus
    while combat_en_cours(persos_restants, opposants_restants):
        tour_de_combat(persos_restants, opposants_restants)
    if tous_vaincus(opposants_restants):  # noqa: SIM103
        return True
    return False


def combat_en_cours(persos_restants, opposants_restants):
    if tous_vaincus(persos_restants):
        return False
    if tous_vaincus(opposants_restants):  # noqa: SIM103
        return False
    return True


def tour_de_combat(persos_restants, opposants_restants):
    # le gagnant du duel reste en tête avec ses HP, le perdant sort de sa file :
    # on affronte donc les opposants un par un, dans l'ordre
    perso = persos_restants[0]
    opposant = opposants_restants[0]
    print(f"{perso['nom']} affronte {opposant['nom']}")
    if duel(perso, opposant):
        opposants_restants.pop(0)
    else:
        persos_restants.pop(0)


def attaquer(attaquant, defenseur):
    defenseur["hp"] -= calculer_degats(attaquant, defenseur)
    if not est_vivant(defenseur):
        print(f"{defenseur['nom']} est vaincu")


def duel(perso, opposant):
    # le perso frappe en premier, l'opposant ne riposte que s'il est encore vivant
    while est_vivant(perso) and est_vivant(opposant):
        attaquer(perso, opposant)
        if est_vivant(opposant):
            attaquer(opposant, perso)
    return est_vivant(perso)


def calculer_degats(attaquant, defenseur):
    degats = math.floor(
        attaquant["attaque"] - defenseur["defense"] / 2
    )  # Limite combat trop long ex. Gérard x Jo (130 tours sans)
    if degats < 1:
        return 1
    return degats


def est_vivant(perso):
    if perso["hp"] > 0:  # noqa: SIM103
        return True
    return False


def tous_vaincus(restants):
    if len(restants) == 0:  # noqa: SIM103
        return True
    return False


if __name__ == "__main__":
    try:
        lancer_jeu()
    except KeyboardInterrupt:
        print("À bientôt")
