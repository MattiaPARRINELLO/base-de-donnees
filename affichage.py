from rich.console import Console
from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.table import Table

import bdd
import catalogue
from constantes import AUCUN_SCORE, NOMBRE_SCORES_AFFICHES
from predicats import est_vivant

console = Console()


def formater_perso(perso):
    return (
        f"{perso['nom']} HP: {perso['hp']} ATT: {perso['attaque']} "
        f"DEF: {perso['defense']} ARME: {perso['arme']}"
    )


def afficher_perso_formate(perso, index):
    print(f"{index}. {formater_perso(perso)}")


def afficher_liste_persos(liste):
    index = 1
    for perso in liste:
        afficher_perso_formate(perso, index)
        index += 1


def choix_persos():
    return [
        (formater_perso(perso), perso) for perso in catalogue.persos.values()
    ]


def afficher_personnages():
    afficher_liste_persos(catalogue.persos.values())


def afficher_score(score, index):
    print(
        f"{index}. {score['pseudo']} - "
        f"{score['opposants_vaincus']} vaincus - "
        f"{score['date_partie']:%d/%m/%Y %H:%M:%S}"
    )


def afficher_scores():
    scores = bdd.lire_scores(NOMBRE_SCORES_AFFICHES)
    if len(scores) == 0:
        print(AUCUN_SCORE)
        return
    index = 1
    for score in scores:
        afficher_score(score, index)
        index += 1


def afficher_meilleur_score():
    score = bdd.lire_meilleur_score()
    if score is None:
        print(AUCUN_SCORE)
        return
    print(f"Record : {score['pseudo']} - {score['opposants_vaincus']} vaincus")


def afficher_coup(attaquant, degats):
    console.print(
        f"[italic]{attaquant['nom']} frappe avec {attaquant['arme']} "
        f"et inflige {degats} dégâts[/]"
    )


def afficher_echange(perso, opposant, degats_perso, degats_opposant):
    afficher_coup(perso, degats_perso)
    if degats_opposant > 0:
        afficher_coup(opposant, degats_opposant)


def barre_vie(combattant):
    return ProgressBar(
        total=combattant["hp_max"],
        completed=max(combattant["hp"], 0),
        width=20,
    )


def ajouter_ligne(table, combattant, degats):
    table.add_row(
        combattant["nom"],
        str(degats),
        f"{max(combattant['hp'], 0)}/{combattant['hp_max']}",
        barre_vie(combattant),
    )


def construire_table_round(perso, opposant, degats_perso, degats_opposant):
    table = Table(title="Round", title_justify="left")
    table.add_column("Combattant")
    table.add_column("Dégâts", justify="right")
    table.add_column("HP", justify="right")
    table.add_column("Vie", width=22)
    ajouter_ligne(table, perso, degats_perso)
    ajouter_ligne(table, opposant, degats_opposant)
    return table


def afficher_vaincus(perso, opposant):
    if not est_vivant(opposant):
        console.print(f"[bold red]{opposant['nom']} est vaincu[/]")
    if not est_vivant(perso):
        console.print(f"[bold red]{perso['nom']} est vaincu[/]")


def afficher_affrontement(perso, opposant):
    console.print(
        f"[bold]{perso['nom']}[/] affronte [bold]{opposant['nom']}[/]"
    )


def afficher_round(perso, opposant, degats_perso, degats_opposant):
    afficher_echange(perso, opposant, degats_perso, degats_opposant)
    table = construire_table_round(
        perso, opposant, degats_perso, degats_opposant
    )
    console.print(Panel(table))
    afficher_vaincus(perso, opposant)


def afficher_resultat(victoire):
    if victoire:
        print("Victoire")
        return
    print("Défaite")
