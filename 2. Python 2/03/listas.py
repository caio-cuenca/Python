valores = []
tipo = type(valores)
print(tipo) # <class 'list'>

lista = [0, 1, 2, 3, "x"]
teste = 6 in lista
teste2 = 1 in lista
print(teste) # False
print(teste2) # True

teste3 = "a" in "banana"
print(teste3) # True

print(lista) #[0, 1, 2, 3, 'x']
print(lista[4]) # x

numeros = [10, 20, 30]
print(min(numeros)) # 10
print(max(numeros)) # 30

invertido = [20, 15, 25]
print(min(invertido)) # 15
print(max(invertido)) # 25

print(len(invertido)) #3

invertido.append(30)
print(invertido) # [20, 15, 25, 30]

print(invertido.pop()) # 30
print(invertido) # [20, 15, 25]

exemplo = [ 0, 0, 0, 1, 2, 3, 4]
print(exemplo.count(0)) # 3
print(exemplo.index(2)) # 4