class Calculadora:
    def somar(self, a, b):
        return a + b

    def subtrair(self, a, b):
        return a - b

calc = Calculadora()
print(f"Soma: {calc.somar(5, 3)}")
print(f"Subtração: {calc.subtrair(10, 7)}")