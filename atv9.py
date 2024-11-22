class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def verificar_aprovacao(self):
        if self.nota >= 7:
            print(f"{self.nome} está aprovado(a)!")
        else:
            print(f"{self.nome} está reprovado(a).")

aluno = Aluno("João", 8)
aluno.verificar_aprovacao()