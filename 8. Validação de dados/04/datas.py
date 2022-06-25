from datetime import datetime, timedelta
from datas_br import DatasBr

print(datetime.today())

# dd/mm/yyyy

hoje = datetime.today()
hoje_ano = hoje.strftime("%Y")
hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")

print(hoje)
print(hoje_ano)
print(hoje_formatado)

print(type(hoje))
print(type(hoje_formatado))

