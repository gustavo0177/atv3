class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self, outro_nome):
        print(f"Olá, {outro_nome}! Eu sou {self.nome}.")

pessoa = Pessoa("Maria")
pessoa.cumprimentar("João")
