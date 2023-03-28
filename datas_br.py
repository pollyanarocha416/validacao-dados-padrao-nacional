from datetime import datetime, timedelta


class DatasBr:
    def __init__(self) -> None:
        self.momento_cadastro = datetime.today()
    
    def __str__(self) -> str:
        return self.format_data()

    def mes_cadastro(self) -> list[int]:
        meses_ano = [
            "janeiro", "fevereiro", "marco", "Abril", "Maio", 
            "Junho", "Julho", "Agosto", "Setembro", "Outubro", 
            "Novembro", "Dezembro"]
        mes_cadastro = self.momento_cadastro.month -1
        return meses_ano[mes_cadastro]

    def dia_semana(self) -> list[int]:
        dia_semana_lista = [
            "segunda", "terça", "quarta", 
            "quinta", "sexta", "sabado", 
            "domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dia_semana_lista[dia_semana]

    def format_data(self) -> str:
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self) -> timedelta:
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
