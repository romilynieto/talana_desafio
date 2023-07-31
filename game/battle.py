import common.constants as constants

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
    if len(mov) == 1 and mov == "D" and player == constants.PLAYER1:
        return "avanza"
    elif len(mov) == 1 and mov == "A" and player == constants.PLAYER2:
        return "avanza"
    elif len(mov) >= 1:
        return "se mueve"
    else:
        return ""