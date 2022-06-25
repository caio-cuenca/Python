

teste = "abcde"
inicio = teste.find("bc")

valor = teste[inicio + len("bc") + 1:]
print(valor)