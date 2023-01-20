import random

baraja_española = {
    # OROS/COINS.
    "G01": {"literal": "Ace of Coins", "value": 1, "priority": 4, "realValue": 1},
    "G02": {"literal": "Two of Coins", "value": 2, "priority": 4, "realValue": 2},
    # ...
    "G12": {"literal": "King of Coins", "value": 12, "priority": 4, "realValue": 0.5},

    # COPAS/CUPS.
    "C01": {"literal": "Ace of Cups", "value": 1, "priority": 3, "realValue": 1},
    "C02": {"literal": "Two of Cups", "value": 2, "priority": 3, "realValue": 2},
    # ...
    "C12": {"literal": "King of Cups", "value": 12, "priority": 3, "realValue": 0.5},

    # SWORDS/ESPADAS.
    "S01": {"literal": "Ace of Swords", "value": 1, "priority": 2, "realValue": 1},
    "S02": {"literal": "Two of Swords", "value": 2, "priority": 2, "realValue": 2},
    # ...
    "S12": {"literal": "King of Swords", "value": 12, "priority": 2, "realValue": 0.5},

    # BASTOS/CLUBS
    "B01": {"literal": "Ace of Clubs", "value": 1, "priority": 1, "realValue": 1},
    "B02": {"literal": "Two of Clubs", "value": 2, "priority": 1, "realValue": 2},
    # ...
    "B12": {"literal": "King of Clubs", "value": 12, "priority": 1, "realValue": 0.5}
}

# Repartir una carta a un jugador
def repartir_carta(jugador,):
    carta = random.choice(list(baraja_española.items()))
    print(f"Jugador {jugador}: {carta[1]['literal']}")
    save =print( f"Jugador {jugador}: {carta[1]['realValue']}")
    return (carta[1]['priority'], carta[1]['value'])

# Repartir cartas a dos jugadores
prioridad_jugador_1, value_jugador_1 = repartir_carta("Jugador 1")
prioridad_jugador_2, value_jugador_2 = repartir_carta("Jugador 2")
#bot es jugador 2 y jugador es jugador 1
if prioridad_jugador_1 > prioridad_jugador_2:
    print("Jugador es la banca")
    banca = 1
elif prioridad_jugador_1 < prioridad_jugador_2:
    print("bot es la banca")
    banca = 2
else:
    if prioridad_jugador_1 == prioridad_jugador_2:
        if value_jugador_1 < value_jugador_2:
            print("bot es la banca")
            banca = 2
        else:
            print("jugador 1 es la banca")    
            banca = 1
ronda =1

