class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def __str__(self):
        return "Código {}, Saldo {}".format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print(conta1 == conta2)

contas = [conta1]
print(conta1 in contas)
print(conta2 in contas)
