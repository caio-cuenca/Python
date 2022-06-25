
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
        # if not self.url
        if self.url == "":
            raise ValueError("A URL está vazia")
        # if self.url.startswith("https"):
        #     raise "A URL começa com https"
        # if self.get_base().endswith("/cambio"):
        #     raise "Estamos na página de câmbio"

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

# extrator_url = ExtratorURL
# extrator_url = ExtratorURL(None)
extrator_url = ExtratorURL("https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100")
valor = extrator_url.get_valor("quantidade")
print(valor)