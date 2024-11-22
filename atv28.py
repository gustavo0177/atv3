class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_saldos(self):
        for i, conta in enumerate(self.contas):
            print(f"Conta {i + 1}: R$ {conta.saldo:.2f}")

conta1 = ContaBancaria(100)
conta2 = ContaBancaria(200)
banco = Banco()
banco.adicionar_conta(conta1)
banco.adicionar_conta(conta2)
banco.listar_saldos()