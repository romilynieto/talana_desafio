def combine_botones(moves, hits):
    joined = []
    for move, hit in zip(moves, hits):
        combined_string = move + hit
        joined.append(combined_string)
    return joined

def contar_botones(comb):
    return sum(1 for c in comb if c in 'AWSD')

def contar_golpes(comb):
    return sum(1 for c in comb if c in 'KP')

def decidir_iniciador(jugador1, jugador2):
    # Obtener las combinaciones de botones de ambos jugadores
    comb_jugador1 = combine_botones(jugador1.datos_comb["movimientos"], jugador1.datos_comb["golpes"])
    comb_jugador2 = combine_botones(jugador2.datos_comb["movimientos"], jugador2.datos_comb["golpes"])

    # Calcular el número de botones y golpes de cada jugador
    botones_jugador1 = contar_botones(comb_jugador1[0])
    botones_jugador2 = contar_botones(comb_jugador2[0])
    golpes_jugador1 = contar_golpes(comb_jugador1[0])
    golpes_jugador2 = contar_golpes(comb_jugador2[0])

    # Comparar el número de botones para determinar el iniciador
    if botones_jugador1 < botones_jugador2:
        return 1
    elif botones_jugador1 > botones_jugador2:
        return 0
    else:
        # En caso de empate en la cantidad de botones, comparar la cantidad de movimientos
        movimientos_jugador1 = len(comb_jugador1) - golpes_jugador1
        movimientos_jugador2 = len(comb_jugador2) - golpes_jugador2

        if movimientos_jugador1 < movimientos_jugador2:
            return 1
        elif movimientos_jugador1 > movimientos_jugador2:
            return 0
        else:
            # En caso de empate en la cantidad de movimientos, comparar la cantidad de golpes
            if golpes_jugador1 < golpes_jugador2:
                return 1
            elif golpes_jugador1 > golpes_jugador2:
                return 0
            else:
                # Si hay empate en todo, inicia el jugador 1
                return 1