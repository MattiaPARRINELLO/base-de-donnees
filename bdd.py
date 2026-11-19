"""
Accès à la base MongoDB des scores.
Aucune fonction ici n'affiche quoi que ce soit : main.py s'en charge.
"""

from datetime import datetime

from pymongo import MongoClient

URI = "mongodb://localhost:27017"
BASE = "arene"
COLLECTION = "scores"

client = MongoClient(URI, serverSelectionTimeoutMS=2000)


def obtenir_collection():
    base = client[BASE]
    return base[COLLECTION]


def initialiser_base():
    collection = obtenir_collection()
    collection.create_index([("opposants_vaincus", -1)])


def enregistrer_score(pseudo, victoire, opposants_vaincus):
    collection = obtenir_collection()
    document = {
        "pseudo": pseudo,
        "victoire": victoire,
        "opposants_vaincus": opposants_vaincus,
        "date_partie": datetime.now(),
    }
    collection.insert_one(document)


def lire_scores(limite):
    collection = obtenir_collection()
    scores = collection.find().sort("opposants_vaincus", -1).limit(limite)
    return list(scores)


def lire_meilleur_score():
    collection = obtenir_collection()
    return collection.find_one(sort=[("opposants_vaincus", -1)])


if __name__ == "__main__":
    initialiser_base()
    scores = lire_scores(5)
    print(len(scores), "score(s) enregistré(s)")
    for score in scores:
        print(score)
