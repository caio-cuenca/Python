
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

# class Playlist(list):
#
#     def __init__(self, nome, programas):
#         self.nome = nome
#         super().__init__(programas)
#         self.programas = programas

    # def tamanho(self):
    #     return len(self.programas)

class Playlist:

    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

vingadores = Filme("Vingadores: Guerra Infinita", 2018, 130)
atlanta = Serie("Atlanta", 2018, 2)
tmep = Filme("Todo Mundo em Pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)

vingadores.like()
tmep.like()
tmep.like()
tmep.like()
tmep.like()
demolidor.like()
demolidor.like()
atlanta.like()
atlanta.like()
atlanta.like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
fim_de_semana = Playlist("Fim de Semana", filmes_e_series)

# for programa in playlist_fim_de_semana.programas:
#     print(programa)

for programa in fim_de_semana.listagem:
    print(programa)

print("Tamanho da playlist: ", len(fim_de_semana.listagem))

print(demolidor in fim_de_semana.listagem)