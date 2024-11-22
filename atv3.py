

class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Ano: {self.ano}")


carro = Carro("Toyota", 2020)
carro.exibir_informacoes()