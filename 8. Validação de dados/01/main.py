from cpf import CPF

# cpf = 15616987913
# cpf = str(cpf)
# tamanho = len(cpf)
# print(tamanho)

cpf = 15616987913
cpf = str(cpf)
objeto_cpf = CPF(cpf)
print(objeto_cpf)

# fatia_um = cpf[0:3]
# fatia_dois = cpf[3:6]
# fatia_tres = cpf[6:9]
# fatia_quatro = cpf[9:11]
# print(fatia_um)
# print(fatia_dois)
# print(fatia_tres)
# print(fatia_quatro)
#
# cpf_formatado = "{}.{}.{}-{}".format(fatia_um, fatia_dois, fatia_tres, fatia_quatro)
# print(cpf_formatado)