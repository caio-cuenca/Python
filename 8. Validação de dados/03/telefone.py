import re

padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "numero 2126451234 e 2136451234"

resposta = re.findall(padrao, texto)
resposta2 = re.search(padrao, texto)

print(resposta)
print(resposta2.group())

padrao3 = "([0-9]{2})([0-9]{4,5})([0-9]{4})"
resposta3 = re.findall(padrao3, texto)
print(resposta3)

resposta4 = re.search(padrao3, texto)
print(resposta4.group())
print(resposta4.group(1))
print(resposta4.group(2))

padrao4 = "([0-9]{2})?([0-9]{4,5})([0-9]{4})"
texto2 = "12345678"
resposta5 = re.search(padrao4, texto2)
print(resposta5)

