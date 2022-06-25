from collections import defaultdict

aparicoes = defaultdict(int)
print(aparicoes)

texto = "Testando um dois teste do texto"
texto.lower()

for palavra in texto.split():
    aparicoes[palavra] += 1

print(aparicoes)

class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)

contas[15]
print(contas[20])

aparicoes2 = defaultdict()
aparicoes2 = Counter(texto.split())
print(aparicoes2)