import random


def play():
    player=input("Selecciona una de las opciones:\n'pi' para piedra.\n'pa' para papel.\n'ti' para tijera.\n").lower()
    computadora=random.choice(['pi','pa','ti'])
    if player==computadora:
        return"¡Empate!"
    if player_gana(player,computadora):
        return '¡Ganaste!'
    return '¡Perdiste!'


def player_gana(jugador, oponente):
    if ((jugador=='pi' and oponente=='ti') or (jugador=='pa' and oponente=='pi') or (jugador=='ti' and oponente=='pa')):
        return True
    else:
        return False


print(play())