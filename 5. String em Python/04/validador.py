# https://www.bytebank.com.br/cambio
import re

url = "https://www.bytebank.com.br/cambio"
padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao.match(url)

if not match:
    raise ValueError("A URL não é válida")
else:
    print("A URL é válida")
