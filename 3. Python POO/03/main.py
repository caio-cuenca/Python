class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O Saldo de {} é: {}".format(self.titular, self.saldo))

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
