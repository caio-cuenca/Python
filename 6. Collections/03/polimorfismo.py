class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[Código: {}, Saldo: {}]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):

    def passar_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passar_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

print(Conta(88))

conta16 = ContaCorrente(16)
conta16.depositar(1000)
conta16.passar_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.depositar(1000)
conta17.passar_mes()
print(conta17)

contas = [conta16, conta17]

for i in contas:
    i.passar_mes()
    print(i)