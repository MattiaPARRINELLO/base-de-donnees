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
    si pseudo_valide():
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
    
"""

"""
afficher_liste_perso_tronquee(a_tronquer):
    liste = []
    pour chaque persos en tant que perso:
        si perso pas dans a_tronquer:
            afficher_perso_formaté()
            liste.ajouter(perso)
        else:
            continuer
    retourner liste
"""
