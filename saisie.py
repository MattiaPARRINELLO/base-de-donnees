import questionary


def demander_choix(message, entrees, valider=None):
    choix = [
        questionary.Choice(titre, value=valeur) for titre, valeur in entrees
    ]
    if valider is None:
        return questionary.select(message, choices=choix).unsafe_ask()
    return questionary.checkbox(
        message, choices=choix, validate=valider
    ).unsafe_ask()


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
