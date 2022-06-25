idades = [39, 18, 15, 27]

print(28 in idades)
print(15 in idades)

if 15 in idades:
    idades.remove(15)

print(idades)

idades.insert(0, 20)

print(idades)

idades2 = [20, 39, 18]

idades2.append([27, 19])

print(idades2)

for elemento in idades2:
    print(elemento)

idades3 = [20,39,18]
idades3.extend([27, 19])
print(idades3)

for i in idades3:
    print(i + 1)

idades4 = []

for i in idades3:
    idades4.append(i + 1)

print(idades4)

idades5 = [(i + 1) for i in idades3]
print(idades5)

idades6 = [(i) for i in idades3 if i > 21]
print(idades6)
