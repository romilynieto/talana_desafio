import common.constants as constants
from game.special_atack import AtaqueEspecial
from game.battle import ejecutar_accion

class Arnaldor:
    nombre =  "Arnaldor"
    tipo_player = constants.PLAYER2
    Remuyuken_Arnaldor = AtaqueEspecial("conecta un Remuyuken", constants.SPECIAL_MOVES_ARNALDOR[0], 3)
    Taladoken_Arnaldor = AtaqueEspecial("conecta un Taladoken", constants.SPECIAL_MOVES_ARNALDOR[1], 2)
    ataques = [Remuyuken_Arnaldor, Taladoken_Arnaldor]
    puntos_salud = 6
    datos_comb = {}
    def __init__(self,datos_comb):
        self.datos_comb = datos_comb

    def ejecutar_combo(moves, hit):
        comb = moves + hit
        ataque = "", 0
        for item in Arnaldor.ataques:
            if comb.find(item.combinacion) > -1:
                ataque = item.nombre, item.danio

        if ataque[0] == "" and ataque[1] == 0:
            ataque = ejecutar_accion(constants.PLAYER2, moves, hit)

        return ataque