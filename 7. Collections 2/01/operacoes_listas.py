
usuarios_data = [15, 23, 43, 56]

usuarios_machine = [13, 23, 42, 56]

assistiram =[]
assistiram.extend(usuarios_data)
print("assisitriam:", assistiram)

assistiram2 = usuarios_data.copy()
print("assistiram2", assistiram2)

assistiram2.extend(usuarios_machine)
print("assistiram2.extend:", assistiram2)
print("len(assistiram2):", len(assistiram2))

print("set(assistiram2):", set(assistiram2))

print("set([1, 2, 3]):", set([1, 2, 3]))
print("set([1, 2, 3, 1]):", set([1, 2, 3, 1]))
print("{4, 1, 2, 3, 1}:", {4, 1, 2, 3, 1})
print("type({1, 2}):", type({1, 2}))
print("\n")

for i in set(assistiram2):
    print(i)

print("\n")
print("set(usuarios_data) | set(usuarios_machine):", set(usuarios_data) | set(usuarios_machine))
print("set(usuarios_data) & set(usuarios_machine):", set(usuarios_data) & set(usuarios_machine))
print("set(usuarios_data) - set(usuarios_machine):", set(usuarios_data) - set(usuarios_machine))
print("set(usuarios_data) ^ set(usuarios_machine):", set(usuarios_data) ^ set(usuarios_machine))

print("15 in (set(usuarios_data) - set(usuarios_machine)):", 15 in (set(usuarios_data) - set(usuarios_machine)))
print("23 in (set(usuarios_data) - set(usuarios_machine)):", 23 in (set(usuarios_data) - set(usuarios_machine)))