lass Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


 retangulo = Retangulo(5, 10)
print(f"Área do retângulo: {retangulo.calcular_area()}")