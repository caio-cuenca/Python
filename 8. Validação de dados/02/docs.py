from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def criar_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos incorreta!")

class DocCpf:

    def __init__(self, documento):
        if self.validar(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.formatar

    def validar(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise  ValueError("Quantidade de dígitos inválida")

    def formatar(self):
        fatia_um = self.cpf[0:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:11]
        return "{}.{}.{}-{}".format(fatia_um, fatia_dois, fatia_tres, fatia_quatro)

class DocCnpj:

    def __init__(self, documento):
        if self.validar(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!")

    def __str__(self):
        return self.formatar

    def validar(self, documento):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida")

    def formatar(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

