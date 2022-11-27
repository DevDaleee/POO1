class AnimalTerrestre:
    def __init__(self):
        self.habitat = "Terra"
    def andar(self):
        print("Andando...")

class AnimalAquatico:
    def __init__(self):
        self.habitat = "Água"
        
    def nadar(self):
        print('Nadando...')

class Anfibio(AnimalTerrestre, AnimalAquatico):
    def __init__ (self):
        AnimalAquatico.__init__(self)
        AnimalTerrestre.__init__(self)
        super().__init__()
    def andar(self):
        print("Anfibio Andando")

sapo = Anfibio()
print(Anfibio.mro())

"""
print(sapo.habitat)
sapo.andar()
sapo.nadar()
"""