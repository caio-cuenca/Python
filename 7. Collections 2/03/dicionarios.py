aparicoes = {
    "Guilherme" : 1,
    "cachorro" : 2,
    "nome" : 2,
    "vindo" : 1,
}

print("type(aparicoes): ", type(aparicoes))

print("aparicoes['Guilherme']:", aparicoes["Guilherme"])

print(aparicoes)

aparicoes2 = dict(Guilherme = 1, cachorro = 2)
print(aparicoes2)

aparicoes["Carlos"] = 1
print(aparicoes)

aparicoes["Carlos"] = 2
print(aparicoes)

del aparicoes["Carlos"]
print(aparicoes)

print("'cachorro' in aparicoes:", "cachorro" in aparicoes)

print("\n")
for elemento in aparicoes:
    print(elemento)

print("\n")
for elemento in aparicoes.keys():
    print(elemento)

print("\n")
for elemento in aparicoes.values():
    print(elemento)

print("\n")
for elemento in aparicoes.items():
    print(elemento)

print("\n")
for chave, valor in aparicoes.items():
    print(chave, "=", valor)

print("\n")
print("['palavra {}'.format(chave) for chave in aparicoes.keys()]:", ["palavra {}".format(chave) for chave in aparicoes.keys()])