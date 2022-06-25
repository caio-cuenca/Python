from datetime import datetime, timedelta
from datas_br import DatasBr

numero = 1
string = "um"

# print(len(numero)) não existe
print(len(string))

hoje = datetime.today()
amanha = datetime.today() + timedelta(days = 1, hours = 20)

print(amanha - hoje)