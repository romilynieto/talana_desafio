from game.battle import ejecutar_accion

class Figther:
    def __init__(self, nombre, tipo_player, ataques, puntos_salud, datos_combate):
        self.nombre = nombre
        self.tipo_player = tipo_player
        self.ataques = ataques
        self.puntos_salud = puntos_salud
        self.datos_combate = datos_combate

    def ejecutar_combo(self, moves, hit):
        comb = moves + hit
        ataque = "", 0
        for item in self.ataques:
            if comb.find(item.combinacion) > -1:
                ataque = item.nombre, item.danio

        if ataque[0] == "" and ataque[1] == 0:
            ataque = ejecutar_accion(self.tipo_player, moves, hit)

        return ataque