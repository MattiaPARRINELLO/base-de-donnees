def est_vivant(perso):
    if perso["hp"] <= 0:
        return False
    return True


def tous_vaincus(restants):
    if len(restants) > 0:
        return False
    return True
