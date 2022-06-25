
class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[Código: {}, Saldo: {}]".format(self.codigo, self.saldo)

gui = ContaCorrente(15)
print(gui)
gui.depositar(500)
print(gui)

dani = ContaCorrente(47685)
dani.depositar(1000)
print(dani)

contas = [gui, dani]
print(contas)

for i in contas:
    print(i)

contas2 = [gui, dani, gui]
print(contas2[0])
gui.depositar(100)
print(contas2[0] == contas2[2])
print(contas2[0] is contas2[2])

contas2[2].depositar(300)
print(gui)
