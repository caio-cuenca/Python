
class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

vingadores = Filme("Vingadores: Guerra Infinita", 2018, 130)
vingadores.like()

print(vingadores.nome, " - ", vingadores.duracao, ": ", vingadores.likes)

atlanta = Serie("Atlanta", 2018, 2)

atlanta.like()
atlanta.like()

print("{} - {}: {}".format(atlanta.nome, atlanta.temporadas, atlanta.likes))