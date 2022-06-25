
class Teste:

    def __init__(self, itens):
        self.itens = itens

    @property
    def listagem(self):
        return self.itens

    def __getitem__(self, item):
        return self.itens[item]

    def __str__(self):
        return "{}".format(self.itens)

    def __len__(self):
        return len(self.itens)

teste = Teste([1, 2, 3])

print(teste)

print(teste.listagem)

print(teste[1])

print(len(teste.listagem))

print(len(teste))

