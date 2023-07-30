import common.constants as constants
from game.special_atack import AtaqueEspecial
from game.battle import Batlle

class Tonyn:
    nombre =  "Tonyn"
    tipo_player = constants.PLAYER1
    Taladoken_Tonyn = AtaqueEspecial("usa un Taladoken", constants.SPECIAL_MOVES_TONYN[0], 3)
    Remuyuken_Tonyn = AtaqueEspecial("usa un Remuyuken", constants.SPECIAL_MOVES_TONYN[1], 2)
    ataques = [Taladoken_Tonyn, Remuyuken_Tonyn]
    puntos_salud = 6
    datos_comb = {}
    def __init__(self,datos_comb):
        self.datos_comb = datos_comb

    def ejecutar_combo(moves, hit):
        comb = moves + hit
        ataque = "", 0
        for item in Tonyn.ataques:
            if comb.find(item.combinacion) > -1:
                ataque = item.nombre, item.danio

        if ataque[0] == "" and ataque[1] == 0:
            ataque = Batlle.ejecutar_accion(Batlle, constants.PLAYER1, moves, hit)

        return ataque