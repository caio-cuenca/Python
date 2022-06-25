
texto = "Testando um dois teste do texto"
texto.lower()
print("texto.lower():", texto.lower())

print("texto.split():", texto.split())

aparicoes = {}

for palavra in texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1

print("aparicoes:", aparicoes)

from collections import defaultdict

aparicoes2 = defaultdict()
print(aparicoes2)


