class ConversorMoeda:
    def __init__(self, taxa_cambio):
        self.taxa_cambio = taxa_cambio

    def converter_dolar_para_real(self, dolares):
        return dolares * self.taxa_cambio

conversor = ConversorMoeda(5.20)
print(f"100 dólares em reais: R$ {conversor.converter_dolar_para_real(100):.2f}")