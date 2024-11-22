class Carro:
    def __init__(self, marca, combustivel=0):
        self.marca = marca
        self.combustivel = combustivel

    def abastecer(self, litros):
        self.combustivel += litros
        print(f"{litros} litros adicionados. Combustível atual: {self.combustivel} litros.")

    def verificar_combustivel(self):
        print(f"Combustível atual: {self.combustivel} litros.")

carro = Carro("Ford")
carro.abastecer(20)
carro.verificar_combustivel()