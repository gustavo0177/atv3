class Veiculo:
    def __init__(self, modelo, velocidade=0):
        self.modelo = modelo
        self.velocidade = velocidade

    def aumentar_velocidade(self, incremento):
        self.velocidade += incremento
        print(f"Velocidade do {self.modelo} agora é {self.velocidade} km/h")

# Testando a classe Veículo
veiculo = Veiculo("Carro")
veiculo.aumentar_velocidade(20)
 