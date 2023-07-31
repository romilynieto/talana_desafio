# Talana Kombat JRPG version 0.0.1
# player1 = Tonynn Stallone
# player2 = Arnaldor Shuatseneguer

from colorama import Fore, init
from colorama import Back, init
from itertools import zip_longest
from player.arnaldor import Arnaldor
from player.tonyn import Tonyn
from common.util import Util
from game.battle import Batlle
import common.constants as constants

init()

# Metodo para obtener JSON de la Pelea
# datos_combate: Parametro que contiene el JSON de movimientos y golpes de los 2 jugadores
def inicializar_players(datos_combate):

    tonyn = Tonyn(datos_combate["player1"])
    arnaldor = Arnaldor(datos_combate["player2"])

    if Util.decidir_iniciador(Util,tonyn, arnaldor) == 1:
        return elaborar_info_pelea(tonyn, arnaldor)
    else:
        return elaborar_info_pelea(arnaldor, tonyn)

# Metodo para generar el informe del resultado de la Pelea
# player_A: Es el primero en ejecutar movimiento (Puede ser Tonyn o Arnaldor)
# player_B: Ejecutara movimiento despues del Player_A
def elaborar_info_pelea(player_A, player_B):

    #obteniendo movimientos y golpes player A
    player_A_moves = player_A.datos_comb["movimientos"]
    player_A_punches = player_A.datos_comb["golpes"]

    #obteniendo movimientos y golpes player A
    player_B_moves = player_B.datos_comb["movimientos"]
    player_B_punches = player_B.datos_comb["golpes"]

    # print de inicio de batalla
    print()
    print(Fore.WHITE + Back.LIGHTMAGENTA_EX + constants.TEXT_BATALLA_INICIA + Fore.RESET + Back.RESET)
    print()

    # Asignando cantidad de puntos de vida
    playerB_energy = player_B.puntos_salud
    playerA_energy = player_A.puntos_salud

    # Iterando la cantidad de movimientos dentro de los arrays de movimientos y golpes
    # Se usa zip_longest para iterar el mayor numero de veces que contiene un array
    for pA_move, pA_punch, pB_move, pB_punch in zip_longest(player_A_moves, player_A_punches, player_B_moves, player_B_punches, fillvalue=""):
        
        # Obteniendo movimiento y daño de cada accion de jugador  
        moveA, damage1 = procesar_jugador(player_A.tipo_player, pA_move.upper(), pA_punch.upper())
        moveB, damage2 = procesar_jugador(player_B.tipo_player, pB_move.upper(), pB_punch.upper())

        # Se registra el daño para el segundo jugador ya que es el primero en recibir golpe
        playerB_energy -= damage1

        # Se imprime el movimiento ejecutado por el playerA
        print(Fore.GREEN + constants.TEXT_MARGEN + constants.TEXT_VIÑETA + player_A.nombre + " " + moveA + Fore.RESET)
        
        # Si el playerB pierde sus puntos de energia acaba el combate
        if playerB_energy <= 0:
            print()
            return print(Fore.BLACK + Back.LIGHTBLUE_EX + constants.TEXT_MARGEN + player_A.nombre + constants.TEXT_GANADOR, playerA_energy, constants.TEXT_ENERGIA_RESTANTE + Fore.RESET + Back.RESET)
        
        # Se registra el daño para el primer jugador ya que es el segundo en recibir golpe
        playerA_energy -= damage2

        # Se imprime el movimiento ejecutado por el playerB
        print(Fore.BLUE + constants.TEXT_MARGEN + constants.TEXT_VIÑETA + player_B.nombre + " " + moveB + Fore.RESET)
        print()

        # Si el playerA pierde sus puntos de energia acaba el combate
        if playerA_energy <= 0:
            print()
            return print(Fore.BLACK + Back.LIGHTBLUE_EX + constants.TEXT_MARGEN + player_B.nombre + constants.TEXT_GANADOR, playerB_energy, constants.TEXT_ENERGIA_RESTANTE + Fore.RESET + Back.RESET)

    # Al no tener ningun vencedor se declara empate        
    return print(Fore.BLACK + Back.LIGHTBLUE_EX + constants.TEXT_MARGEN  + constants.TEXT_EMPATE + Fore.RESET + Back.RESET)


# Metodo para Ejecutar golpes y ataques Especiales          
def procesar_jugador(player, move, hit):
    if player == constants.PLAYER1:
        return Tonyn.ejecutar_combo(move, hit)
    else:
        return Arnaldor.ejecutar_combo(move, hit)


###################################################################################################################################
# Ejemplos de uso
###################################################################################################################################

# Resultado 1: Arnaldor Gana la pelea y aun le queda 2 de energía  
fight_data1 = {
    "player1": {"movimientos": ["D","DSD","S","DSD","SD"], "golpes": ["K","P","P","K","P"]},
    "player2": {"movimientos": ["SA","SA","SA","ASA","SA"], "golpes": ["K","","K","P","P"]}
}

# Resultado 2: Gana Tony
fight_data2 = {
    "player1":{"movimientos":["SDD", "DSD", "SA", "DSD"] ,"golpes":["K", "P", "K", "P"]}, 
    "player2":{"movimientos":["DSD", "WSAW", "ASA", "", "ASA", "SA"],"golpes":["P", "K", "K", "K", "P", "k"]}
}

# Resultado 3: Gana Arnaldor
fight_data3 = {
    "player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]}, 
    "player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "K", "K", "K"]}
}

# Resultado 4: Empate
fight_data4 = {
    "player1":{"movimientos":["DSD", "S"] ,"golpes":[ "P", ""]}, 
    "player2":{"movimientos":["", "ASA", "DA", "AAA", "", "SA"],"golpes":["P", "", "P", "", "", ""]}
}

inicializar_players(fight_data1)
inicializar_players(fight_data2)
inicializar_players(fight_data3)
inicializar_players(fight_data4)