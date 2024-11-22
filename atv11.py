class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depositado: R$ {valor}. Saldo atual: R$ {self.saldo}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Sacado: R$ {valor}. Saldo atual: R$ {self.saldo}")
        else:
            print("Saldo insuficiente.")

# Testando a classe ContaBancaria
conta = ContaBancaria(100)
conta.depositar(50)
conta.sacar(30)
conta.sacar(150)