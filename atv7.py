class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        return self.preco


produto = Produto("Celular", 1500)
print(f"Preço com desconto: R$ {produto.aplicar_desconto(10):.2f}")
