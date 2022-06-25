idades = [15, 87, 32, 65, 56, 32, 49, 37]

usuarios = [
    ("Gui", 37, 1981),
    ("Dani", 31, 1987),
    ("Paulo", 39, 1979)
]

print("sorted(idades):", sorted(idades))

print("list(reversed(idades)):", list(reversed(idades)))

print("sorted(idades, reverse = True):", sorted(idades, reverse = True))

print("list(reversed(sorted(idades))):", list(reversed(sorted(idades))))

print("idades.sort()", idades.sort())
print(idades)