from operator import attrgetter

idades = [15, 87, 32, 65, 56, 32, 49, 37]

nomes = ["Guilherme", "Daniela", "Paulo"]

print("sorted(nomes):", sorted(nomes))

nomes2 = ["guilherme", "Daniela", "Paulo"]

print("sorted(nomes2):", sorted(nomes2))

class ContaSalario:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  # def extrair_saldo(conta):
  #   return conta._saldo

  def depositar(self, valor):
    self._saldo += valor

  def __str__(self):
    return "[Código: {}, Saldo: {}]".format(self._codigo, self._saldo)

  def __lt__(self, other):
      return self._saldo < other._saldo

conta_gui = ContaSalario(17)
conta_gui.depositar(500)

conta_dani = ContaSalario(3)
conta_dani.depositar(1000)

conta_paulo = ContaSalario(133)
conta_paulo.depositar(510)

contas = [conta_gui, conta_dani, conta_paulo]

print("\nfor i in contas:")
for i in contas:
    print(i)

# for conta in sorted(contas, key = extrair_saldo):
#     print(conta)

print("\nfor conta in sorted(contas, key = attrgetter('_saldo')):")
for conta in sorted(contas, key = attrgetter("_saldo")):
    print(conta)

print("\nconta_gui < conta_dani:", conta_gui < conta_dani)
print("conta_gui > conta_dani:", conta_gui > conta_dani)

print("\nfor conta in sorted(contas):")
for conta in sorted(contas):
    print(conta)

print("\nfor conta in sorted(contas, reverse = True):")
for conta in sorted(contas, reverse = True):
    print(conta)