usuarios = {1, 3, 76, 34, 52, 13, 17}
print("len(usuarios):", len(usuarios))

usuarios.add(13)
print("len(usuarios):", len(usuarios))

usuarios.add(765)
print("len(usuarios):", len(usuarios))

usuarios = frozenset(usuarios)
print("usuarios:", usuarios)
print("type(usuarios):", type(usuarios))

texto = "testando um dois testando"
texto.split()
set(texto.split())
print("set(texto.split()):", set(texto.split()))