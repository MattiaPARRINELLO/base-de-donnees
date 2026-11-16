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
fonction afficher_menu
    pseudo = demander_pseudo()
    equipe = creer_equipe()
"""

"""
fonction demander_pseudo():
    pseudo = entrée("Entre ton pseudo :")
    si pseudo_valide(pseudo):
        retourner pseudo
    sinon:
        afficher("Pseudo non valide")
        retourner(demander_pseudo)
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
    choix = entree("Choix du personnage : ")
    si choix_valide(choix, liste):
        retourner liste[entier(choix) - 1]
    
    sinon:
        afficher("Choix non valide")
        retourner demander_perso(equipe)
    
"""

"""
fonction pseudo_valide(pseudo):
    si longueur(pseudo) > 40 ou longueur(pseudo) < 3:
        retourne faux
    
    sinon:
        retourne vrai
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
