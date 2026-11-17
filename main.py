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


"""
fonction lancer_jeu():
    tant que vrai:
        choix = afficher_menu()
        si choix == "1":
            demarrer_partie()
        sinon si choix == "2":
            afficher_liste_persos(persos_disponibles([]))
        sinon:
            retourner   
"""

"""
fonction afficher_menu():
    tant que vrai:
        afficher("1. Nouvelle partie")
        afficher("2. Voir les personnages")
        afficher("3. Quitter")
        choix = entree("Ton choix : ")
        si choix_valide(choix, 1, 3):
            retourner choix
        afficher("Choix invalide")
"""

"""
fonction choix_valide(choix, minimum, maximum):
    si choix est un nombre:
        choix = entier(choix)
        si minimum <= choix et choix <= maximum:
            retourner vrai
    retourner faux
"""

"""
fonction demarrer_partie():
    pseudo = demander_pseudo()
    equipe = creer_equipe()
    liste_opposants = tirer_opposant()
    si combattre(equipe, liste_opposants):
        afficher("Victoire")
    sinon: 
        afficher("Défaite")
"""

"""
fonction demander_pseudo():
    tant que vrai:
        pseudo = entrée("Entre ton pseudo :")
        si pseudo_valide(pseudo):
            retourner pseudo
        afficher("Pseudo non valide")
"""

"""
fonction pseudo_valide(pseudo):
    si longueur(pseudo) > 40 ou longueur(pseudo) < 3:
        retourner faux
    
    sinon:
        retourner vrai
"""

"""
fonction creer_equipe():
    equipe = []
    while longueur(equipe) < 3:
        equipe.ajouter(demander_perso(equipe))
"""

"""
fonction demander_perso(equipe):
    liste = persos_disponibles(equipe)
    afficher_liste_persos(liste)
    tant que vrai:
        choix = entree("Choix du personnage : ")
        si choix_valide(choix, 1, longueur(liste)):
            retourner liste[entier(choix) - 1]
        afficher("Choix non valide")
    
"""

"""
fonction persos_disponibles(a_tronquer):
    liste = []
    pour chaque persos en tant que perso:
        si perso['nom'] pas dans les noms de a_tronquer:
            liste.ajouter(perso)
    retourner liste
"""

"""
fonction afficher_liste_persos(liste):
    index = 1
    pour chaque perso dans liste:
        afficher_perso_formate(perso, index)
        index += 1 
"""

"""
fonction afficher_perso_formate(perso, index):
    afficher("{index}. {perso['nom']} HP: {perso['hp']} ATT: {perso['attaque']} DEF: {perso['defense']} ARME: {perso['arme']}")
"""

"""
fonction tirer_opposant():
    cles = liste des clé de opposants
    melanger(cles)
    liste = []
    pour chaque cle dans cles:
        liste.ajouter(copier(opposants[cle]))
    retourner liste
"""

"""
fonction combattre(equipe, liste_opposants):
    i_perso = 0
    i_opposant = 0
    tant que i_perso < longueur(equipe) et i_opposant < longueur(liste_opposants):
        afficher(equipe[i_perso]['nom'], "affronte", liste_opposants[i_opposant]['nom'])
        si duel(equipe[i_perso], liste_opposants[i_opposant]):
            i_opposant = i_opposant + 1 
        sinon:
            i_perso = i_perso + 1
    si i_opposant >= longueur(liste_opposants):
        retourner vrai
    retourner faux
"""

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

"""
fonction calculer_degats(attaquant, defenseur):
    degats = arrondi_inferieur(attaquant['attaque'] - (defenseur['defense'] / 2)) #Limite combat trop long ex. Gérard x Jo (130 tours sans)
    si degats < 1:
        retourner 1
    retourner degats    
"""
