import requests
from acesso_cep import BuscaEndereco

cep = "01001000"
objeto_cep = BuscaEndereco(cep)
print(objeto_cep)

r = requests.get("https://viacep.com.br/ws/01001000/json/")
print(r)
print(r.text)

teste = objeto_cep.acessar()
print(teste)
print(type(teste))
print(dir(teste))
print(teste.text)
print(teste.json())
print(type(teste.text))
print(type(teste.json()))
print(teste.json()["bairro"])

novo = objeto_cep.acessar_viacep()
print(novo)