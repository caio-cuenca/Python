def foo(valor):
    if valor:
        print("Verdadeiro")
    else:
        print("Falso")

foo("")
# Falso

foo(None)
# Falso

foo(0)
# Falso

foo(1)
# Vdd

foo(" ")
# Vdd