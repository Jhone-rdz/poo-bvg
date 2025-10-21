class Cliente:
    def __init__(self, nome, idade, saldo):
        self.__nome = nome
        self.__idade = idade
        self.__saldo = saldo

    def mostrar_informacoes(self):
        print(f"nome: {self.__nome} /n idade: {self.__idade} /n saldo: {self.__saldo}")

    def atualizar_saldo(self, valor):
        self.__saldo = valor
