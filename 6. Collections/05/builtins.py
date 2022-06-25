
idades = [15, 87, 32, 65, 56, 32, 49, 37]

range(len(idades))
print("range(len(idades)):", range(len(idades)))

for i in range(len(idades)):
    print(i, idades[i])

print("enumerate(idades):", enumerate(idades))

print("list(range(len(idades)):", list(range(len(idades))))

print("list(enumerate(idades)):", list(enumerate(idades)))

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades): # unpacking da tupla
    print(indice, idade)

usuarios = [
    ("Gui", 37, 1981),
    ("Dani", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, ano in usuarios:
    print(nome)

for nome, _, _ in usuarios:
    print(nome)

