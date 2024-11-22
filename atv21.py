class Livro:
    def __init__(self, titulo, autor, estoque):
        self.titulo = titulo
        self.autor = autor
        self.estoque = estoque

    def exibir_detalhes(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Estoque: {self.estoque}")

livro = Livro("1984", "George Orwell", 10)
livro.exibir_detalhes()