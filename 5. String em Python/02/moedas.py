
url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"
print(url)

# Separa a base
interrogacao = url.find("?")
url_base = url[0:interrogacao]
print(url_base)

#Separa os parâmetros
url_parametros = url[interrogacao + 1:]
print(url_parametros)

# print(url.find("x"))

# Retorna a moeda de origem
busca = "moedaOrigem"
indice_busca = url_parametros.find(busca)
# print(indice_busca)

indice_valor = indice_busca + len(busca) + 1
valor = url_parametros[indice_valor:]
print(valor)

# Retorna a moeda de destino
busca2 = "moedaDestino"
indice_busca2 = url_parametros.find(busca2)

indice_valor2 = indice_busca2 + len(busca2) + 1
e_comercial = url_parametros.find("&")
valor2 = url_parametros[indice_valor2:e_comercial]
print(valor2)
