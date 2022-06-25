import re

padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbcc rodrigo123@gmail.com.br testando123"
resposta = re.search(padrao, texto)
print(resposta.group())

padrao2 = "\w{5,50}@[a-z]{3,10}.com.br"
resposta2 = re.search(padrao2, texto)
print(resposta2.group())