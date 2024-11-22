class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


pessoa = Pessoa("Ana", 25)
pessoa.exibir_informacoes()