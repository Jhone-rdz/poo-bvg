class Carro:
    def __init__(self, ano, marca, modelo, cor, placa):
        self.ano = ano
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self._placa = placa

    def exibir_detalhes(self):
        print(f"As informações do carro são: Ano: {self.ano}, Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Placa: {self.get_placa()}")

    def atualizar_cor(self, nova_cor):
        self.cor = nova_cor

    def get_placa(self):
        return self._placa

    def atualizar_placa(self, nova_placa):
        self._placa = nova_placa
    
