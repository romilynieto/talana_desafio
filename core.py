# Talana Kombat JRPG version 0.0.1

# player1 = Tonynn Stallone
# player2 = Arnaldor Shuatseneguer

from colorama import Fore, init
init()


SPECIAL_MOVES_Tonyn = ["DSDP", "SDK"]
SPECIAL_MOVES_ARNALDOR = ["SAK", "ASAP"]
PLAYER1 = 1
PLAYER2 = 2

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

# Mostrar el resultado
#print("joined:", joined)

# Datos de los jugadores
""" jugador1 = {
    "nombre": "Jugador 1",
    "combinacion": "P"
}

jugador2 = {
    "nombre": "Jugador 2",
    "combinacion": "A"
} """

# Decidir quién inicia la batalla
#iniciador = decidir_iniciador(jugador1, jugador2)

# Mostrar el resultado
#print(f"El jugador que inicia la batalla es: {iniciador}")


def decidir_iniciador(jugador1, jugador2):
    # Obtener las combinaciones de botones de ambos jugadores
    comb_jugador1 = combine_botones(jugador1.datos_comb["movimientos"], jugador1.datos_comb["golpes"])
    comb_jugador2 = combine_botones(jugador2.datos_comb["movimientos"], jugador2.datos_comb["golpes"])

    # Calcular el número de botones y golpes de cada jugador
    botones_jugador1 = contar_botones(comb_jugador1)
    botones_jugador2 = contar_botones(comb_jugador2)
    golpes_jugador1 = contar_golpes(comb_jugador1)
    golpes_jugador2 = contar_golpes(comb_jugador2)


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
        elaborar_info_pelea(tonyn, arnaldor)
    else:
        elaborar_info_pelea(arnaldor, tonyn)

###################################################################################################################################

def elaborar_info_pelea(player_A, player_B):

    player_A_moves = player_A.datos_comb["movimientos"]
    player_A_punches = player_A.datos_comb["golpes"]

    player_B_moves = player_B.datos_comb["movimientos"]
    player_B_punches = player_B.datos_comb["golpes"]

    print("---------procesando batalla----------")

    playerB_energy = player_B.puntos_salud
    playerA_energy = player_A.puntos_salud

    for pA_move, pA_punch, pB_move, pB_punch in zip(player_A_moves, player_A_punches, player_B_moves, player_B_punches):

        moveA, damage1 = procesar_jugador(player_A.tipo_player, pA_move.upper(), pA_punch.upper())
        moveB, damage2 = procesar_jugador(player_B.tipo_player, pB_move.upper(), pB_punch.upper())

        playerB_energy -= damage1

        #print("---movimientos de Player A--")
        print(Fore.GREEN + player_A.nombre + " " + moveA + Fore.RESET)
        print("Puntos de vida " + player_B.nombre + ": " + str(max(playerB_energy, 0)))
        
        if playerB_energy <= 0:
            print(player_A.nombre +  " Gana la pelea y aún le queda", playerA_energy, "de energía")
            return player_A.nombre
        
        playerA_energy -= damage2

        #print("---movimientos de Player B--")
        print(Fore.BLUE + player_B.nombre + " " + moveB + Fore.RESET)
        print("Puntos de vida " + player_A.nombre + ": " + str(max(playerA_energy, 0)))

        if playerA_energy <= 0:
            print(player_B.nombre + " Gana la pelea y aún le queda", playerB_energy, "de energía")
            return player_B.nombre
        
    return print("empate")


def ejecutar_accion(player, moves, hit):
    accion = "No hace nada", 0
    mov = procesar_movimiento(player, moves)
    
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
    elif len(mov) > 1:
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


def procesar_JSON(datos_combate):
    player1_moves = datos_combate["player1"]["movimientos"]
    player1_punches = datos_combate["player1"]["golpes"]

    player2_moves = datos_combate["player2"]["movimientos"]
    player2_punches = datos_combate["player2"]["golpes"]

    print("---------procesando batalla----------")

    player1_energy = 6
    player2_energy = 6

    for p1_move, p1_punch, p2_move, p2_punch in zip(player1_moves, player1_punches, player2_moves, player2_punches):
  
        #player1_combinations = p1_move + p1_punch
        #player2_combinations = p2_move + p2_punch

        move1, damage1 = procesar_jugador(PLAYER1, p1_move.upper(), p1_punch.upper())
        move2, damage2 = procesar_jugador(PLAYER2, p2_move.upper(), p2_punch.upper())

        player2_energy -= damage1
        player1_energy -= damage2

        print("---movimientos de Tonyn--")
        print(Fore.GREEN + "Tonyn " + move1 + Fore.RESET)
        print("---movimientos de Arnaldor--")
        print(Fore.BLUE + "Arnaldor "+ move2 + Fore.RESET)

        if player2_energy <= 0:
            print("Tonyn Gana la pelea y aún le queda", max(player1_energy, 0), "de energía")
            return "Tonyn"
        elif player1_energy <= 0:
            print("Arnaldor Gana la pelea y aún le queda", max(player2_energy, 0), "de energía")
            return "Arnaldor"
    
    return print("empate")


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

#ganador = talana_kombat_jrpg(fight_data)
#print("Resultado final:", ganador)

#procesar_JSON(fight_data1)

# falta el turno de quien golpea primero 

print(inicializar_players(fight_data3))

# falta que la pelea continue cuando un jugador se queda sin moviemintops pero el otro si tiene aun ataques