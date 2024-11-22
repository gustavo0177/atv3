class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Duração: {self.duracao} minutos")

# Testando a classe Filme
filme = Filme("Inception", 148)
filme.exibir_detalhes()