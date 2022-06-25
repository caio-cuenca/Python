from validate_docbr import CPF

class Cpf:

    def __init__(self, documento):
        documento = str(documento)
        if self.validar(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

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

    def __str__(self):
        return self.formatar()
