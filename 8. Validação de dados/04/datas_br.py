from datetime import datetime, timedelta

class DatasBr:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formatar()

    def mes_cadastro(self):
        meses_do_ano = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    def dia_semana(self):
        dias_semana = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def formatar(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() - self.momento_cadastro
        return tempo_cadastro