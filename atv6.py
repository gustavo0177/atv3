class Animal:
    def __init__(self, especie, som):
        self.especie = especie
        self.som = som

    def emitir_som(self):
        print(f"O {self.especie} faz: {self.som}")


animal = Animal("Cachorro", "Au Au")
animal.emitir_som()