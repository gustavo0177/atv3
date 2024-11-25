class Eletrodomestico:
    def __init__(self, nome, potencia):
        self.nome = nome
        self.potencia = potencia

    def ligar(self):
        print(f"{self.nome} está ligado, consumindo {self.potencia}W.")


eletro = Eletrodomestico("Micro-ondas", 1200)
eletro.ligar()
