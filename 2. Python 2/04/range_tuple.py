lista = [2, 5, 2, 8, 5]
palavra = "banana"

print(len(lista)) # 5
print(len(palavra)) # 6

print(min(lista)) # 2
print(min(palavra)) # a

print(lista[3]) # 8
print(palavra[3]) # a

serie = range(0, 10)
print(serie) # range(0, 10)
print(min(serie)) # 0
print(max(serie)) # 9

# tuple, são imutáveis
exemplo = (0, 1, 2, 3)
print(len(exemplo)) # 4

p1 = ("Lucas", 10)
p2 = ("Mateus", 20)
pessoas = [p1, p2]
print(pessoas) # [('Lucas', 10), ('Mateus', 20)]
print(pessoas[0]) # ('Lucas', 10)
print(pessoas[0][1]) # 10

palavras = []
palavras.append("laranja")
palavras.append("limão")
print(palavras) # ['laranja', 'limão']
nova = tuple(palavras)
print(nova) # ('laranja', 'limão')

