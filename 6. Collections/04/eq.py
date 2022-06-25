class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def depositar(self, valor):
        self._saldo += valor

    def __str__(self):
        return "Código {}, Saldo {}".format(self._codigo, self._saldo)

    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False

        return self._codigo == other._codigo

class ContaMultipla(ContaSalario):
    pass


conta1 = ContaSalario(37)
print(conta1)

conta2 = ContaSalario(37)
print("conta1 == conta2:", conta1 == conta2)

contas = [conta1]
print("conta1 in contas:", conta1 in contas)
print("conta2 in contas:", conta2 in contas)

print("conta1 != conta2:", conta1 != conta2)

print("isinstance(ContaSalario(10), ContaSalario):", isinstance(ContaSalario(10), ContaSalario))
print("isinstance(ContaMultipla(10), ContaSalario):", isinstance(ContaMultipla(10), ContaSalario))

