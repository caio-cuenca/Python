import re

class ExtratorURL:

    def __init__(self, url):
        self.url = self.sanitizar(url)
        self.validar()

    def sanitizar(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validar(self):
        if self.url == "":
            raise ValueError("A URL está vazia")

        padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao.match(self.url)

        if not match:
            raise ValueError("A URL não é válida")
        else:
            print("A URL é válida")

    def get_base(self):
        interrogacao = self.url.find("?")
        url_base = self.url[0:interrogacao]
        return url_base

    def get_parametros(self):
        interrogacao = self.url.find("?")
        url_parametros = self.url[interrogacao + 1:]
        return url_parametros

    def get_valor(self, parametro):
        indice_busca = self.get_parametros().find(parametro)
        indice_valor = indice_busca + len(parametro) + 1
        e_comercial = self.get_parametros().find("&", indice_valor)

        if e_comercial == -1:
            return self.get_parametros()[indice_valor:]
        else:
            return self.get_parametros()[indice_valor:e_comercial]

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_parametros() + "\n" + "URL Base: " + self.get_base()

    def __eq__(self, other):
        return self.url == other.url

url = "https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
objeto1 = ExtratorURL(url)

objeto1_origem = objeto1.get_valor("Origem")
objeto1_destino = objeto1.get_valor("Destino")
objeto1_qntdd = int(objeto1.get_valor("quantidade"))

if objeto1_origem == "dolar":
    objeto1_qntdd_conv = objeto1_qntdd * 5
    print(objeto1_qntdd, " dólares são ", objeto1_qntdd_conv, " reais!")
else:
    objeto1_qntdd_conv = objeto1_qntdd / 5
    print(objeto1_qntdd, " reais são ", objeto1_qntdd_conv, " dólares!")