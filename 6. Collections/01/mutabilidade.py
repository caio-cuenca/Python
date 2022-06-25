
def processamento(lista):
    print(len(lista))
    lista.append(13)

idades = [16, 21, 29, 56, 43]
processamento(idades)
print(idades)

def visualiza(lista = []):
    print(len(lista))
    lista.append(13)

visualiza()
visualiza()
visualiza()

def teste(lista = list()):
    print(len(lista))
    lista.append(15)
    print(lista)

teste()
teste()

def exemplo(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(20)

exemplo()
exemplo()
exemplo()

