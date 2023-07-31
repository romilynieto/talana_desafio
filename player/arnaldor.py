import common.constants as constants
from game.special_atack import AtaqueEspecial
from game.battle import ejecutar_accion
from player.figther import Figther  # Importamos la clase padre

class Arnaldor(Figther):  # Heredamos de la clase padre
    def __init__(self, datos_combate):
        # Llamamos al constructor de la clase padre con los valores específicos para Arnaldor
        super().__init__(
            "Arnaldor", 
            constants.PLAYER2, 
            [
                AtaqueEspecial("conecta un Remuyuken", constants.SPECIAL_MOVES_ARNALDOR[0], 3),
                AtaqueEspecial("conecta un Taladoken", constants.SPECIAL_MOVES_ARNALDOR[1], 2)
            ],
            6, 
            datos_combate
        )