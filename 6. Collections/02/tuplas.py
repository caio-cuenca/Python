class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[Código: {}, Saldo: {}]".format(self.codigo, self.saldo)

def depositar_todas(contas):
    for conta in contas:
        conta.depositar(100)

gui = ContaCorrente(15)
gui.depositar(500)

dani = ContaCorrente(47685)
dani.depositar(1000)

contas = [gui, dani]

depositar_todas(contas)
print(contas[0], contas[1])

contas.insert(0, 76)
print(contas[0], contas[1], contas[2])

# tuplas

guilherme = ("Guilherme", 37, 1981)
daniela = ("Daniela", 31, 1987)

# não tem append

alex = (10, 200)

def modificar(tupla):
    item1 = tupla[0]
    item2 = tupla[1] + 100
    return (item1, item2)

alex = modificar(alex)
print(alex)
