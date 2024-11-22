class Relogio:
    def __init__(self, hora, minuto, segundo):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def exibir_horario(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"

relogio = Relogio(14, 30, 15)
print(relogio.exibir_horario())