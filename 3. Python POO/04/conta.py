class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O Saldo de {} é: {}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    # def transferir(self, valor, origem, destino):
        # origem.sacar(valor)
        # destino.depositar(valor)

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
