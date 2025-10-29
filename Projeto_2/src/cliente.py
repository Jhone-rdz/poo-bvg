class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self._cpf = cpf
        self.seguros = []

    def exibir_informacoes(self):
        print(f"Informações do cliente: Nome: {self.nome}, CPF: {self.get_cpf()}")

    def get_cpf(self):
        return self._cpf

    def atualizar_cpf(self, novo_cpf):
        self._cpf = novo_cpf
