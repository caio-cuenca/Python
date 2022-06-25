class CpfCnpj:

    def __init__(self, documento, tipo_documento):
        self.tipo_documento = tipo_documento
        documento = str(documento)
        if tipo_documento == "cpf":
            if self.validar_cpf(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF inválido!")
        elif self.tipo_documento == "cnpj":
            if self.validar_cnpj(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido")

    def validar_cpf(self, documento):
        if len(documento) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
            raise  ValueError("Quantidade de dígitos inválida")

    def formatar_cpf(self):
        fatia_um = self.cpf[0:3]
        fatia_dois = self.cpf[3:6]
        fatia_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:11]
        return "{}.{}.{}-{}".format(fatia_um, fatia_dois, fatia_tres, fatia_quatro)

    def __str__(self):
        if self.tipo_documento == "cpf":
            return self.formatar_cpf()
        elif self.tipo_documento == "cnpj":
            return self.formatar_cnpj()

    def validar_cnpj(self, cnpj):
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de dígitos inválida")

    def formatar_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)