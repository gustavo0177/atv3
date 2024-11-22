class Pessoa:
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

pessoa = Pessoa(70, 1.75)
print(f"IMC: {pessoa.calcular_imc():.2f}")