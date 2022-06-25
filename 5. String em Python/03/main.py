# url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
url = " "

# Sanitização da URL
url = url.replace(" ", "")

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia")

interrogacao = url.find("?")
url_base = url[0:interrogacao]
url_parametros = url[interrogacao + 1:]

busca = "moedaDestino"
indice_busca = url_parametros.find(busca)
indice_valor = indice_busca + len(busca) + 1
e_comercial = url_parametros.find("&", indice_valor)

if e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:e_comercial]

print(valor)
