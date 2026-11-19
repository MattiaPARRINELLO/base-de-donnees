"""
Jeu de combat au tour par tour, joué en console.
Les scores sont enregistrés dans MongoDB via le module bdd.
"""

import math
import random
import time

import questionary
from rich.console import Console
from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.table import Table

import bdd

console = Console()

persos = {
    "gerard": {
        "nom": "Gérard",
        "hp": 150,
        "attaque": 30,
        "defense": 35,
        "arme": "une chaise pliante",
    },
    "ketty": {
        "nom": "Ketty",
        "hp": 85,
        "attaque": 46,
        "defense": 12,
        "arme": "un rouleau à pâtisserie rouillé",
    },
    "bruno": {
        "nom": "Bruno",
        "hp": 200,
        "attaque": 26,
        "defense": 45,
        "arme": "son corps, littéralement",
    },
    "sacha": {
        "nom": "Sacha",
        "hp": 75,
        "attaque": 55,
        "defense": 8,
        "arme": "des insultes très précises",
    },
    "nadine": {
        "nom": "Nadine, la RH",
        "hp": 110,
        "attaque": 34,
        "defense": 25,
        "arme": "un entretien de recadrage",
    },
    "kevin": {
        "nom": "Kevin, 19 ans",
        "hp": 95,
        "attaque": 40,
        "defense": 15,
        "arme": "son fond d'écran de motivation",
    },
    "mamie_huguette": {
        "nom": "Mamie Huguette",
        "hp": 120,
        "attaque": 32,
        "defense": 30,
        "arme": "son déambulateur lancé à pleine vitesse",
    },
    "le_chien": {
        "nom": "Le Chien",
        "hp": 90,
        "attaque": 42,
        "defense": 18,
        "arme": "des crocs et aucune morale",
    },
    "jean_michel": {
        "nom": "Jean-Michel",
        "hp": 100,
        "attaque": 36,
        "defense": 20,
        "arme": "une perceuse sans fil",
    },
    "fatou": {
        "nom": "Fatou, la factrice",
        "hp": 105,
        "attaque": 38,
        "defense": 22,
        "arme": "un colis trop lourd",
    },
}

opposants = {
    "tonton_jo": {
        "nom": "Tonton Jo",
        "hp": 135,
        "attaque": 33,
        "defense": 32,
        "arme": "son camion, en marche arrière",
    },
    "la_voisine": {
        "nom": "La Voisine",
        "hp": 95,
        "attaque": 38,
        "defense": 15,
        "arme": "un balai et beaucoup de temps libre",
    },
    "le_stagiaire": {
        "nom": "Le Stagiaire",
        "hp": 55,
        "attaque": 16,
        "defense": 10,
        "arme": "un badge qui dit AUTORISÉ",
    },
    "mireille": {
        "nom": "Mireille, 68 ans",
        "hp": 85,
        "attaque": 48,
        "defense": 18,
        "arme": "un sac à main plus lourd qu'un parpaing",
    },
    "le_beau_frere": {
        "nom": "Le Beau-frère",
        "hp": 120,
        "attaque": 36,
        "defense": 24,
        "arme": "des conseils non sollicités",
    },
    "le_videur": {
        "nom": "Le Videur",
        "hp": 150,
        "attaque": 30,
        "defense": 30,
        "arme": "une oreillette et beaucoup d'autorité",
    },
    "le_prof_de_sport": {
        "nom": "Le Prof de sport",
        "hp": 115,
        "attaque": 40,
        "defense": 20,
        "arme": "un sifflet et zéro pitié",
    },
    "la_belle_mere": {
        "nom": "La Belle-mère",
        "hp": 130,
        "attaque": 34,
        "defense": 28,
        "arme": "des remarques à double tranchant",
    },
    "le_chat": {
        "nom": "Le Chat",
        "hp": 70,
        "attaque": 50,
        "defense": 12,
        "arme": "des griffes et beaucoup de mépris",
    },
    "le_commercial": {
        "nom": "Le Commercial",
        "hp": 105,
        "attaque": 37,
        "defense": 23,
        "arme": "un argumentaire agressif",
    },
}


TAILLE_EQUIPE = 3
NOMBRE_OPPOSANTS = 4
NOMBRE_SCORES_AFFICHES = 10
PAUSE_ROUND = 0.8


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
    return demander_selection("Ton choix : ", choix)


def demander_selection(message, choix, valider=None):
    if valider is None:
        return questionary.select(message, choices=choix).unsafe_ask()
    return questionary.checkbox(
        message, choices=choix, validate=valider
    ).unsafe_ask()


def afficher_personnages():
    afficher_liste_persos(persos.values())


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
    liste_opposants = tirer_opposants()
    victoire = combattre(equipe, liste_opposants)
    afficher_resultat(victoire)
    enregistrer_partie(pseudo, victoire, liste_opposants)


def afficher_resultat(victoire):
    if victoire:
        print("Victoire")
        return
    print("Défaite")


def enregistrer_partie(pseudo, victoire, liste_opposants):
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
    pseudo = pseudo.strip()  # on retire les espaces
    if len(pseudo) > 40:
        return False
    if len(pseudo) < 3:
        return False
    return True


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
        questionary.Choice(formater_perso(perso), value=perso)
        for perso in persos.values()
    ]
    equipe = demander_selection(
        f"Choisis tes {TAILLE_EQUIPE} personnages : ",
        choix,
        valider_equipe,
    )
    # copie pour chaque perso : sinon leurs HP baissent dans le catalogue
    return [dict(perso, hp_max=perso["hp"]) for perso in equipe]


def afficher_liste_persos(liste):
    index = 1
    for perso in liste:
        afficher_perso_formate(perso, index)
        index += 1


def formater_perso(perso):
    return (
        f"{perso['nom']} HP: {perso['hp']} ATT: {perso['attaque']} "
        f"DEF: {perso['defense']} ARME: {perso['arme']}"
    )


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
            f"{index}. {score['pseudo']} - "
            f"{score['opposants_vaincus']} vaincus - "
            f"{score['date_partie']:%d/%m/%Y %H:%M:%S}"
        )
        index += 1


def afficher_meilleur_score():
    score = bdd.lire_meilleur_score()
    if score is None:
        print("Aucun score enregistré")
        return
    print(f"Record : {score['pseudo']} - {score['opposants_vaincus']} vaincus")


def afficher_affrontement(perso, opposant):
    console.print(
        f"[bold]{perso['nom']}[/] affronte [bold]{opposant['nom']}[/]"
    )


def afficher_round(perso, opposant, degats_perso, degats_opposant):
    table = Table(title="Round", title_justify="left")
    table.add_column("Combattant")
    table.add_column("Dégâts", justify="right")
    table.add_column("HP", justify="right")
    table.add_column("Vie", width=22)
    combattants = ((perso, degats_perso), (opposant, degats_opposant))
    for combattant, degats in combattants:
        table.add_row(
            combattant["nom"],
            str(degats),
            f"{max(combattant['hp'], 0)}/{combattant['hp_max']}",
            ProgressBar(
                total=combattant["hp_max"],
                completed=max(combattant["hp"], 0),
                width=20,
            ),
        )
    console.print(
        f"[italic]{perso['nom']} frappe avec {perso['arme']} "
        f"et inflige {degats_perso} dégâts[/]"
    )
    if degats_opposant > 0:
        console.print(
            f"[italic]{opposant['nom']} riposte avec {opposant['arme']} "
            f"et inflige {degats_opposant} dégâts[/]"
        )
    console.print(Panel(table))
    if not est_vivant(opposant):
        console.print(f"[bold red]{opposant['nom']} est vaincu[/]")
    if not est_vivant(perso):
        console.print(f"[bold red]{perso['nom']} est vaincu[/]")


def tirer_opposants():
    cles = list(opposants.keys())
    random.shuffle(cles)
    liste = []
    for cle in cles[:NOMBRE_OPPOSANTS]:
        # même raison que pour l'équipe : on copie pour ne pas
        # abîmer les opposants du catalogue
        liste.append(dict(opposants[cle], hp_max=opposants[cle]["hp"]))
    return liste


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


def combat_en_cours(persos_restants, opposants_restants):
    if tous_vaincus(persos_restants):
        return False
    if tous_vaincus(opposants_restants):
        return False
    return True


def tour_de_combat(persos_restants, opposants_restants):
    # le gagnant du duel reste en tête avec ses HP, le perdant
    # sort de sa file : on affronte les opposants un par un
    perso = persos_restants[0]
    opposant = opposants_restants[0]
    afficher_affrontement(perso, opposant)
    if duel(perso, opposant):
        opposants_restants.pop(0)
    else:
        persos_restants.pop(0)


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
        afficher_round(perso, opposant, degats_perso, degats_opposant)
        time.sleep(PAUSE_ROUND)
    return est_vivant(perso)


def calculer_degats(attaquant, defenseur):
    degats = math.floor(
        attaquant["attaque"] - defenseur["defense"] / 2
    )  # Limite combat trop long ex. Gérard x Jo (130 tours sans)
    if degats < 1:
        return 1
    return degats


def est_vivant(perso):
    if perso["hp"] <= 0:
        return False
    return True


def tous_vaincus(restants):
    if len(restants) > 0:
        return False
    return True


if __name__ == "__main__":
    try:
        lancer_jeu()
    except KeyboardInterrupt:
        print("À bientôt")
