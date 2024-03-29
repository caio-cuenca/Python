endereco = "Rua das Flores, 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

import re

# 5 dígitos + hífen (opcional) + 3 dígitos
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
# padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
# padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)