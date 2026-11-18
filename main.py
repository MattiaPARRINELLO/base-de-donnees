import math
import random

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

"""
fonction lancer_jeu():
    tant que vrai:
        choix = demander_choix_menu()
        si choix == 1:
            demarrer_partie()
        sinon si choix == 2:
            afficher_liste_persos(persos_disponibles([]))
        sinon si choix == 3:
            afficher_scores()
        sinon:
            retourner   
"""


def lancer_jeu():
    bdd.initialiser_base()
    while True:
        afficher_meilleur_score()
        choix = demander_choix_menu()
        if choix == 1:
            demarrer_partie()
        elif choix == 2:
            afficher_liste_persos(persos_disponibles([]))
        elif choix == 3:
            afficher_scores()
        else:
            return


"""
fonction demander_choix_menu():
    afficher("1. Nouvelle partie")
    afficher("2. Voir les personnages")
    afficher("3. Voir les scores)
    afficher("4. Quitter")
    retourner demander_choix(4, "Ton choix : ")
"""


def demander_choix_menu():
    print("1. Nouvelle partie")
    print("2. Voir les personnages")
    print("3. Voir les scores")
    print("4. Quitter")
    return demander_choix(4, "Ton choix : ")


"""
fonction choix_valide(choix, minimum, maximum):
    si choix n'est pas un nombre:
        retourner faux
    choix = entier(choix)
    si minimum > choix ou choix > maximum:
            retourner faux
    retourner vrai
"""


def choix_valide(choix, minimum, maximum):
    if not choix.isdigit():
        return False
    choix = int(choix)
    if minimum > choix or choix > maximum:  # noqa: SIM103
        return False
    return True


"""
fonction demander_choix(nombre_options, message):
    tant que vrai:
        choix = entree(message)
        si choix_valide(choix, 1, nombre_options):
            retourner entier(choix)
        afficher("Choix invalide")
"""


def demander_choix(nombre_options, message):
    while True:
        choix = input(message)
        if choix_valide(choix, 1, nombre_options):
            return int(choix)
        print("Choix invalide")


"""
fonction compter_vaincus(liste_opposants):
    vaincus = 0
    pour chaque opposant dans liste_opposants:
        si opposant['hp'] <= 0:
            vaincus += 1
    retourner vaincus
"""


def compter_vaincus(liste_opposants):
    vaincus = 0
    for opposant in liste_opposants:
        if opposant["hp"] <= 0:
            vaincus += 1
    return vaincus


"""
fonction demarrer_partie():
    pseudo = demander_pseudo()
    equipe = creer_equipe()
    liste_opposants = tirer_opposant()
    victoire = combattre(equipe, liste_opposants) 
    si victoire:
        afficher("Victoire")
    sinon: 
        afficher("Défaite")
    vaincus = 0
    pour chaque opposant dans liste_opposants:
        si opposant['hp'] <= 0:
            vaincus += 1
    enregistrer score dans la base de données
    afficher(f"Score enregistré : {vaincus} opposant(s) vaincu(s)")
"""


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


"""
fonction demander_pseudo():
    tant que vrai:
        pseudo = entrée("Entre ton pseudo :")
        si pseudo_valide(pseudo):
            retourner pseudo
        afficher("Pseudo non valide")
"""


def demander_pseudo():
    while True:
        pseudo = input("Entre ton pseudo : ").strip()
        if pseudo_valide(pseudo):
            return pseudo
        print("Pseudo non valide")


"""
fonction pseudo_valide(pseudo):
    si longueur(pseudo) > 40 ou longueur(pseudo) < 3:
        retourner faux
    
    sinon:
        retourner vrai
"""


def pseudo_valide(pseudo):
    if len(pseudo) > 40:
        return False
    if len(pseudo) < 3:  # noqa: SIM103
        return False
    else:
        return True


"""
fonction creer_equipe():
    equipe = []
    while equipe_complete(equipe):
        equipe.ajouter(demander_perso(equipe))
"""


def creer_equipe():
    equipe = []
    while not equipe_complete(equipe):
        equipe.append(demander_perso(equipe))
    return equipe


"""
fonction equipe_complete(equipe):
    si longueur equipe >= TAILLE EQUIPE:
        return True
    return False
"""


def equipe_complete(equipe):
    if len(equipe) >= TAILLE_EQUIPE:  # noqa: SIM103
        return True
    return False


"""
fonction demander_perso(equipe):
    liste = persos_disponibles(equipe)
    afficher_liste_persos(liste)
    choix = demander_choix(longueur(liste), "Choix du personnage : ")
    retourner liste[choix - 1]
"""


def demander_perso(equipe):
    liste = persos_disponibles(equipe)
    afficher_liste_persos(liste)
    choix = demander_choix(len(liste), "Choix du personnage : ")
    return liste[choix - 1]


"""
fonction persos_disponibles(a_tronquer):
    liste = []
    pour chaque persos en tant que perso:
        si perso['nom'] pas dans les noms de a_tronquer:
            liste.ajouter(perso)
    retourner liste
"""


def persos_disponibles(a_tronquer):
    nom_pris = []
    for perso in a_tronquer:
        nom_pris.append(perso["nom"])
    liste = []
    for perso in persos.values():
        if perso["nom"] not in nom_pris:
            liste.append(perso)
    return liste


"""
fonction afficher_liste_persos(liste):
    index = 1
    pour chaque perso dans liste:
        afficher_perso_formate(perso, index)
        index += 1 
"""


def afficher_liste_persos(liste):
    index = 1
    for perso in liste:
        afficher_perso_formate(perso, index)
        index += 1


"""
fonction afficher_perso_formate(perso, index):
    afficher("{index}. {perso['nom']} HP: {perso['hp']} ATT: {perso['attaque']} DEF: {perso['defense']} ARME: {perso['arme']}")
"""


def afficher_perso_formate(perso, index):
    print(
        f"{index}. {perso['nom']} HP: {perso['hp']} ATT: {perso['attaque']} DEF: {perso['defense']} ARME: {perso['arme']}"
    )


"""
fonction afficher_score():
    scores = lire_scores(10)
    si longueur(scores) == 0:
        afficher("Aucun score enregistré")
        retourner
    index = 1
    pour chaque score dans scores:
        afficher(f"{index}. {score['pseudo']} - {score['opposants_vaincus']} vaincus - {score['date_partie']}")
        index += 1

"""


def afficher_scores():
    scores = bdd.lire_scores(10)
    if len(scores) == 0:
        print("Aucun score enregistré")
        return
    index = 1
    for score in scores:
        print(
            f"{index}. {score['pseudo']} - {score['opposants_vaincus']} vaincus - {score['date_partie']:%d/%m/%Y %H:%M:%S}"
        )
        index += 1


"""
fonction afficher_meilleur_score():
    score = lire_meilleur_score()
    si score est nul:
        afficher("Aucun score enregistré")
        retourner
    afficher("Record : {score['pseudo']} - {score['opposants_vaincus']} vaincus")
"""


def afficher_meilleur_score():
    score = bdd.lire_meilleur_score()
    if score is None:
        print("Aucun score enregistré")
        return
    print(f"Record : {score['pseudo']} - {score['opposants_vaincus']} vaincus")


"""
fonction tirer_opposant():
    cles = liste des clé de opposants
    mélanger(cles)
    liste = []
    pour chaque cle dans cles:
        liste.ajouter(copier(opposants[cle]))
    retourner liste
"""


def tirer_opposant():
    cles = list(opposants.keys())
    random.shuffle(cles)
    liste = []
    for cle in cles:
        liste.append(dict(opposants[cle]))

    return liste


"""
fonction combattre(equipe, liste_opposants):
    persos_restants = copie de equipe
    opposants_restants = copie de liste_opposants
    tant combat_en_cours(persos_restants, opposants_restants):
        tour_de_combat(persos_restant, opposants_restants)
    si opposant_restant est vide:
        retourner vrai
    retourner faux
"""


def combattre(equipe, liste_opposants):
    persos_restants = list(equipe)
    opposants_restants = list(liste_opposants)
    while combat_en_cours(persos_restants, opposants_restants):
        tour_de_combat(persos_restants, opposants_restants)
    if len(opposants_restants) == 0:  # noqa: SIM103
        return True
    return False


"""
fonction combat_en_cours(persos_restants, opposants_restants):
    si persos_restants est vide:
        retourner faux
    si opposants_restants est vide:
        retourner faux
    retourner vrai
"""


def combat_en_cours(persos_restants, opposants_restants):
    if len(persos_restants) == 0:
        return False
    if len(opposants_restants) == 0:  # noqa: SIM103
        return False
    return True


"""
fonction tour_de_combat(persos_restants, opposants_restants):
    perso = persos_restants[0]
    opposant = opposant_restants[0]
    afficher(perso['nom'], affronte, opposant['nom'])
    si duel(perso, opposant):
        retirer le premier de opposant_restants
    sinon
        retirer le premier de persos_restants
"""


def tour_de_combat(persos_restants, opposants_restants):
    perso = persos_restants[0]
    opposant = opposants_restants[0]
    print(f"{perso['nom']} affronte {opposant['nom']}")
    if duel(perso, opposant):
        opposants_restants.pop(0)
    else:
        persos_restants.pop(0)


"""
fonction attaquer(attaquant, defenseur):
    defenseur['hp'] =  defenseur['hp'] - calculer_degats(attaquant, defenseur)
    si defenseur['hp'] <= 0:
        afficher(defenseur['nom'], "est vaincu")
"""


def attaquer(attaquant, defenseur):
    defenseur["hp"] -= calculer_degats(attaquant, defenseur)
    if defenseur["hp"] <= 0:
        print(f"{defenseur['nom']} est vaincu")


"""
fonction duel(perso, opposant):
    tant que perso['hp'] > 0 et opposant['hp'] > 0:
        opposant['hp'] = opposant['hp'] - calculer_degats(perso, opposant)
        si opposant['hp'] <= 0:
            afficher(opposant['nom'], "est vaincu")
        sinon:
            perso['hp'] = perso['hp'] - calculer_degats(opposant, perso)
            si perso['hp'] <= 0:
                afficher(perso['nom'], "est vaincu")
    retourner perso['hp'] > 0
"""


def duel(perso, opposant):
    while perso["hp"] > 0 and opposant["hp"] > 0:
        attaquer(perso, opposant)
        if opposant["hp"] > 0:
            attaquer(opposant, perso)
    return perso["hp"] > 0


"""
fonction calculer_degats(attaquant, defenseur):
    degats = arrondi_inferieur(attaquant['attaque'] - (defenseur['defense'] / 2)) #Limite combat trop long ex. Gérard x Jo (130 tours sans)
    si degats < 1:
        retourner 1
    retourner degats    
"""


def calculer_degats(attaquant, defenseur):
    degats = math.floor(
        attaquant["attaque"] - defenseur["defense"] / 2
    )  # Limite combat trop long ex. Gérard x Jo (130 tours sans)
    if degats < 1:
        return 1
    return degats


if __name__ == "__main__":
    lancer_jeu()
