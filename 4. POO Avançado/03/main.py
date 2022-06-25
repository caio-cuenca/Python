
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

    def imprimir(self):
        print("{} - {} - {}".format(self._nome, self.ano, self._likes))

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return "{} - {} - {} min - {} likes ".format(self._nome, self.ano, self.duracao, self._likes)

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return "{} - {} - {} temporadas - {} likes".format(self._nome, self.ano, self.temporadas, self._likes)

vingadores = Filme("Vingadores: Guerra Infinita", 2018, 130)
vingadores.like()

# print(vingadores.nome, " - ", vingadores.duracao, ": ", vingadores.likes)

atlanta = Serie("Atlanta", 2018, 2)

atlanta.like()
atlanta.like()

# print("{} - {}: {}".format(atlanta.nome, atlanta.temporadas, atlanta.likes))

filmes_e_series = [vingadores, atlanta]

# for programa in filmes_e_series:
    # detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
    # print("{} - {}: {}".format(programa.nome, detalhes, programa.likes))

# for programa in filmes_e_series:
    # if hasattr(programa, "duracao"):
        # detalhes = programa.duracao
    # else:
        # detalhes = programa.temporadas
    # print("{} - {}: {}".format(programa.nome, detalhes, programa.likes))

# for programa in filmes_e_series:
    # programa.imprimir()

for programa in filmes_e_series:
    print(programa)