class Seguro:
    def __init__(self, carro, cliente, valor, regencia):
        self.carro = carro
        self.cliente = cliente
        self.valor = valor
        self.regencia = bool(regencia)


    def calcular_valor(self, base_valor, taxa):
        self.valor = base_valor * (1 + taxa)
        return self.valor

    def verificar_vigencia(self):
        return "Regência ativa" if self.regencia else "Regência inativa"
            
        