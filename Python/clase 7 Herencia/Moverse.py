class Pato:
    def __init__(self, nombre, especie="Pato"):
        self.nombre = nombre
        self.especie = especie

    def volar(self):
        return f"El {self.especie} {self.nombre} está volando."

    def nadar(self):
        return f"El {self.especie} {self.nombre} está nadando."

# Uso:
mi_pato = Pato("Pistucia")
print(mi_pato.volar()) # El Pato Donald está volando.
print(mi_pato.nadar()) # El Pato Donald está nadando.