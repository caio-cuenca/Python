from docs import Documento
from validate_docbr import CNPJ
from validate_docbr import CPF

exemplo_cnpj = "35379838000112"
cnpj = CNPJ()
print(cnpj.validate(exemplo_cnpj))

documento = CpfCnpj(exemplo_cnpj, "cnpj")

documento2 = Documento.criar_documento(exemplo_cnpj)
print(documento2)
