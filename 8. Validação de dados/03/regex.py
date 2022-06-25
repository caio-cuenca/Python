import re

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta)
print(resposta.group())

padrao2 = "[0-9][a-z]{2}[0-9]"
texto2 = "123 1ac2 1cc aa1"
resposta2 = re.search(padrao2, texto2)
print(resposta2)
print(resposta2.group())