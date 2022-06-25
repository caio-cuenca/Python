from operator import attrgetter

from functools import total_ordering

@total_ordering
class ContaSalario:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def depositar(self, valor):
    self._saldo += valor

  def __str__(self):
    return "[Código: {}, Saldo: {}]".format(self._codigo, self._saldo)

  def __lt__(self, other):
      if self._saldo != other._saldo:
        return self._saldo < other._saldo
      return self._codigo < other._codigo

conta_gui = ContaSalario(1700)
conta_gui.depositar(500)

conta_dani = ContaSalario(3)
conta_dani.depositar(1000)

conta_paulo = ContaSalario(133)
conta_paulo.depositar(500)

contas = [conta_gui, conta_dani, conta_paulo]

print("\n")
print("for conta in sorted(contas, key = attrgetter('_saldo')):")
for conta in sorted(contas, key = attrgetter("_saldo", "_codigo")):
    print(conta)

print("\n")
print("for conta in sorted(contas):")
for conta in sorted(contas):
    print(conta)

print("\n")
print("conta_gui <= conta_dani:", conta_gui <= conta_dani)
