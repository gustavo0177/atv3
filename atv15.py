class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

quadrado = Quadrado(5)
print(f"Área: {quadrado.calcular_area()}, Perímetro: {quadrado.calcular_perimetro()}")