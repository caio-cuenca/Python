class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        # self.__codigo_banco = "001"

    def extrato(self):
        print("O Saldo de {} é: R${}".format(self.__titular, self.__saldo))

    def depositar(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def sacar(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor ultrapassou o limite")

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}