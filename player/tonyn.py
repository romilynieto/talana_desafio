import common.constants as constants
from game.special_atack import AtaqueEspecial
from game.battle import ejecutar_accion
from player.figther import Figther  # Importamos la clase padre

class Tonyn(Figther):  # Heredamos de la clase padre
    def __init__(self, datos_combate):
        # Llamamos al constructor de la clase padre con los valores específicos para Tonyn
        super().__init__(
            "Tonyn", 
            constants.PLAYER1, 
            [
                AtaqueEspecial("usa un Taladoken", constants.SPECIAL_MOVES_TONYN[0], 3),
                AtaqueEspecial("usa un Remuyuken", constants.SPECIAL_MOVES_TONYN[1], 2)
            ],
            6, 
            datos_combate
        )