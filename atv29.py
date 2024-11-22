class Jogo:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def iniciar_jogo(self):
        print(f"O jogo {self.nome} começou!")

    def registrar_pontuacao(self, pontos):
        self.pontuacao += pontos
        print(f"Pontuação atual: {self.pontuacao}")

jogo = Jogo("Aventura")
jogo.iniciar_jogo()
jogo.registrar_pontuacao(10)
