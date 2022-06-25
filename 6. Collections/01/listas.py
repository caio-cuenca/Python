# idade1 = 39
# idade2 = 30
# idade3 = 27
# idade4 = 18
#
# print(idade1)
# print(idade2)
# print(idade3)
# print(idade4)

idades = [39, 30, 27, 18]

print(type(idades))
print(len(idades))
print(idades[0])
print(idades)

idades.append(15)

print(idades)
print(idades[4])

for idade in idades:
    print(idade)

idades.remove(30)

print(idades)