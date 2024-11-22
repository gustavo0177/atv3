class Calculadora:
    def __init__(self):
        self.historico = []

    def somar(self, a, b):
        resultado = a + b
        self.historico.append(f"{a} + {b} = {resultado}")
        return resultado

    def exibir_historico(self):
        for operacao in self.historico:
            print(operacao)

calc = Calculadora()
calc.somar(3, 5)
calc.somar(10, 7)
calc.exibir_historico()