class Elevador:
    def __init__(self, total_andares):
        self.andar_atual = 0
        self.total_andares = total_andares

    def subir(self):
        if self.andar_atual < self.total_andares:
            self.andar_atual += 1
        print(f"Subiu para o andar {self.andar_atual}.")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
        print(f"Desceu para o andar {self.andar_atual}.")

elevador = Elevador(5)
elevador.subir()
elevador.descer()