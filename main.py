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
fonction demarrer_partie():
    pseudo = demander_pseudo()
    equipe = creer_equipe()
"""

"""
fonction afficher_menu():
    afficher("1. Nouvelle partie")
    afficher("2. Voir les personnages")
    afficher("3. Quitter")
    retourner entree("Ton choix :")
"""

"""
fonction lancer_jeu():
    tant que vrai:
        choix = afficher_menu()
        si choix == "1":
            demarrer_partie()
        sinon si choix == "2":
            afficher_liste_perso_tronquee([])
        sinon si choix == "3":
            retourner   
        sinon:
            afficher("Choix invalide")
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
fonction creer_equipe():
    equipe = []
    while longueur(equipe) < 3:
        equipe.ajouter(demander_perso(equipe))
"""

"""
fonction demander_perso(equipe):
    liste = afficher_liste_perso_tronquee(equipe)
    tant que vrai:
        choix = entree("Choix du personnage : ")
        si choix_valide(choix, liste):
            retourner liste[entier(choix) - 1]
        afficher("Choix non valide")
    
"""

"""
fonction pseudo_valide(pseudo):
    si longueur(pseudo) > 40 ou longueur(pseudo) < 3:
        retourner faux
    
    sinon:
        retourner vrai
"""

"""
fonction choix_valide(choix, liste):
    si choix n'est pas un nombre:
        retourner faux
    
    si choix < 1 ou choix > longueur(liste):
        retourner faux
    
    retourner vrai
"""

"""
fonction afficher_liste_perso_tronquee(a_tronquer):
    liste = []
    pour chaque persos en tant que perso:
        si perso.nom pas dans nom de a_tronquer:
            liste.ajouter(perso)
            afficher_perso_formate(perso, longueur(liste))
        else:
            continuer
    retourner liste
"""


"""
fonction afficher_perso_formate(perso, index):
    afficher("{index}. {perso['nom']} HP: {perso['hp']} ATT: {perso['attaque']} DEF: {perso['defense']} ARME: {perso['arme']}")
"""


"""
fonction calculer_degats(attaquant, defenseur):
    degats = arrondi_inferieur(attaquant.attaque - (defenseur.defense / 2)) #Limite combat trop long ex. Gérard x Jo (130 tours sans)
    si degats < 1:
        retourner 1
    retourner degats    
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
    tant que i_persso < longueur(equipe) et i_opposant < longueur(liste_opposants):
        perso = equipe[i_perso]
        opposant = liste_opposants[i_opposant]
        afficher(perso['hp'] > 0 et opposant['hp'] > 0):
"""
