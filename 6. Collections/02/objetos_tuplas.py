
guilherme = ("Guilherme", 37, 1981)
daniela = ("Daniela", 31, 1987)

usuarios = [guilherme, daniela]
print(usuarios)

usuarios.append(("Paulo", 39, 1979))
print(usuarios)

print(usuarios[0])
print(usuarios[0][0])

class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[Código: {}, Saldo: {}]".format(self.codigo, self.saldo)

gui = ContaCorrente(15)
gui.depositar(500)

dani = ContaCorrente(47685)
dani.depositar(1000)

contas = (gui, dani)

print(contas)

gui.depositar(100)
contas[0].depositar(100)

for i in contas:
    print(i)