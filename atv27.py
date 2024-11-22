class Animal:
    def __init__(self, especie, movimento):
        self.especie = especie
        self.movimento = movimento

    def mover(self):
        print(f"O {self.especie} {self.movimento}.")

animal = Animal("peixe", "nada")
animal.mover()