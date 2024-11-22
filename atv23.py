class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_aumento(self, percentual):
        self.salario += self.salario * (percentual / 100)
        print(f"Novo salário de {self.nome}: R$ {self.salario:.2f}")

funcionario = Funcionario("Maria", 3000)
funcionario.calcular_aumento(10)