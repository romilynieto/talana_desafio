# Talana Kombat JRPG version 0.0.1

# player1 = Tonynn Stallone
# player2 = Arnaldor Shuatseneguer

from colorama import Fore, init
from colorama import Back, init
from itertools import zip_longest

init()


SPECIAL_MOVES_Tonyn = ["DSDP", "SDK"]
SPECIAL_MOVES_ARNALDOR = ["SAK", "ASAP"]
PLAYER1 = 1
PLAYER2 = 2

TEXT_MARGEN = "   "
TEXT_VIÑETA = "> "
TEXT_PUNTOS = "Puntos de vida "
TEXT_ENERGIA_RESTANTE  = "de energía"
TEXT_GANADOR = " Gana la pelea y aún le queda"
TEXT_EMPATE = "La pelea finalizó con un empate"
TEXT_BATALLA_INICIA = "-------------------------- Inicia la Batalla en Talana Kombat --------------------------"
TEXT_BATALLA_FINALIZA = "------------------------ Fin de la Batalla en Talana Kombat ------------------------"

class AtaqueEspecial:
    def __init__(self,nombre, combinacion, danio):
        self.nombre = nombre
        self.combinacion = combinacion
        self.danio = danio

class Tonyn:
    nombre =  "Tonyn"
    tipo_player = PLAYER1
    Taladoken_Tonyn = AtaqueEspecial("usa un Taladoken", SPECIAL_MOVES_Tonyn[0], 3)
    Remuyuken_Tonyn = AtaqueEspecial("usa un Remuyuken", SPECIAL_MOVES_Tonyn[1], 2)
    ataques = [Taladoken_Tonyn, Remuyuken_Tonyn]
    puntos_salud = 6
    datos_comb = {}
    def __init__(self,datos_comb):
        self.datos_comb = datos_comb

class Arnaldor:
    nombre =  "Arnaldor"
    tipo_player = PLAYER2
    Remuyuken_Arnaldor = AtaqueEspecial("conecta un Remuyuken", SPECIAL_MOVES_ARNALDOR[0], 3)
    Taladoken_Arnaldor = AtaqueEspecial("conecta un Taladoken", SPECIAL_MOVES_ARNALDOR[1], 2)
    ataques = [Remuyuken_Arnaldor, Taladoken_Arnaldor]
    puntos_salud = 6
    datos_comb = {}
    def __init__(self,datos_comb):
        self.datos_comb = datos_comb

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

###################################################################################################################################

def inicializar_players(datos_combate):

    tonyn = Tonyn(datos_combate["player1"])
    arnaldor = Arnaldor(datos_combate["player2"])

    if decidir_iniciador(tonyn, arnaldor) == 1:
        return elaborar_info_pelea(tonyn, arnaldor)
    else:
        return elaborar_info_pelea(arnaldor, tonyn)

###################################################################################################################################

def elaborar_info_pelea(player_A, player_B):

    player_A_moves = player_A.datos_comb["movimientos"]
    player_A_punches = player_A.datos_comb["golpes"]

    player_B_moves = player_B.datos_comb["movimientos"]
    player_B_punches = player_B.datos_comb["golpes"]

    print()
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + TEXT_BATALLA_INICIA + Fore.RESET + Back.RESET)
    print()

    playerB_energy = player_B.puntos_salud
    playerA_energy = player_A.puntos_salud

    for pA_move, pA_punch, pB_move, pB_punch in zip_longest(player_A_moves, player_A_punches, player_B_moves, player_B_punches, fillvalue=""):

        moveA, damage1 = procesar_jugador(player_A.tipo_player, pA_move.upper(), pA_punch.upper())
        moveB, damage2 = procesar_jugador(player_B.tipo_player, pB_move.upper(), pB_punch.upper())

        playerB_energy -= damage1

        print(Fore.GREEN + TEXT_MARGEN + TEXT_VIÑETA + player_A.nombre + " " + moveA + Fore.RESET)
        #print(TEXT_PUNTOS + player_B.nombre + ": " + str(max(playerB_energy, 0)))
        
        if playerB_energy <= 0:
            print()
            return print(Fore.BLACK + Back.LIGHTBLUE_EX + TEXT_MARGEN + player_A.nombre + TEXT_GANADOR, playerA_energy, TEXT_ENERGIA_RESTANTE + Fore.RESET + Back.RESET)
        
        playerA_energy -= damage2

        print(Fore.BLUE + TEXT_MARGEN + TEXT_VIÑETA + player_B.nombre + " " + moveB + Fore.RESET)
        print()
        #print(TEXT_PUNTOS + player_A.nombre + ": " + str(max(playerA_energy, 0)))

        if playerA_energy <= 0:
            print()
            return print(Fore.BLACK + Back.LIGHTBLUE_EX + TEXT_MARGEN + player_B.nombre + TEXT_GANADOR, playerB_energy, TEXT_ENERGIA_RESTANTE + Fore.RESET + Back.RESET)
        
    return print(Fore.BLACK + Back.LIGHTBLUE_EX + TEXT_MARGEN  + TEXT_EMPATE + Fore.RESET + Back.RESET)


def ejecutar_accion(player, moves, hit):
    accion = "se queda quieto", 0
    mov = procesar_movimiento(player, moves)
    
    if len(moves) == 0 and len(hit) == 0:
        return accion
    if len(mov) > 0 and len(hit) > 0:
        accion =  procesar_golpe(hit, mov)
    elif len(mov) > 0 and len(hit) < 1:
        accion = mov, 0
    elif len(mov) == 0:
        accion = procesar_golpe(hit)
    return accion

def procesar_golpe(hit, mov=""):
    if hit == "P" and mov == "":
        return "Conecta un Puñetazo", 1
    elif hit == "K" and mov == "":
        return "Conecta una Patada", 1
    elif hit == "P" and mov != "":
        return mov + " y da " + "un Puñetazo", 1
    elif hit == "K" and mov != "":
        return mov + " y da " +"una Patada", 1
    else:
        return "", 0

def procesar_movimiento(player, mov):
    if len(mov) == 1 and mov == "D" and player == PLAYER1:
        return "avanza"
    elif len(mov) == 1 and mov == "A" and player == PLAYER2:
        return "avanza"
    elif len(mov) >= 1:
        return "se mueve"
    else:
        return ""
   

def ejecutar_combo_tonyn(moves, hit):
    comb = moves + hit
    ataque = "", 0
    for item in Tonyn.ataques:
        if comb.find(item.combinacion) > -1:
            ataque = item.nombre, item.danio

    if ataque[0] == "" and ataque[1] == 0:
        ataque = ejecutar_accion(PLAYER1, moves, hit)

    return ataque

def ejecutar_combo_arnaldor(moves, hit):
    comb = moves + hit
    ataque = "", 0
    for item in Arnaldor.ataques:
        if comb.find(item.combinacion) > -1:
            ataque = item.nombre, item.danio

    if ataque[0] == "" and ataque[1] == 0:
        ataque = ejecutar_accion(PLAYER2, moves, hit)

    return ataque
            
def procesar_jugador(player, move, hit):
    if player == PLAYER1:
        return ejecutar_combo_tonyn(move, hit)
    else:
        return ejecutar_combo_arnaldor(move, hit)


# Ejemplos de uso:

# Resultado: Arnaldor Gana la pelea y aun le queda 2 de energía  
# Obs: En el Word indica que le quedaría 1 de energia pero el calculo esta errado
fight_data1 = {
    "player1": {"movimientos": ["D","DSD","S","DSD","SD"], "golpes": ["K","P","","K","P"]},
    "player2": {"movimientos": ["SA","SA","SA","ASA","SA"], "golpes": ["K","","K","P","P"]}
}

# Resultado Gana Tony
fight_data2 = {
    "player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]}, 
    "player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "k"]}
}

# Resultado Gana Arnaldor
fight_data3 = {
    "player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]}, 
    "player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}
}

# Resultado Gana Arnaldor
fight_data4 = {
    "player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]}, 
    "player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "", "", ""]}
}

inicializar_players(fight_data1)
inicializar_players(fight_data2)
inicializar_players(fight_data3)
inicializar_players(fight_data4)