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


def copier_combattant(combattant):
    return dict(combattant, hp_max=combattant["hp"])
