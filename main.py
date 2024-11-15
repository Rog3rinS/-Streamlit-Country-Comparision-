import psycopg2
import pandas as pd

conn = psycopg2.connect(
    database = "Country",
    host = "localhost",
    user = "postgres",
    password = "1234",
    port = "5432"
)

cursor = conn.cursor()

print(conn.status)

dados = pd.read_sql("SELECT * FROM Dados_Paises", conn)

def get_dataframe():
    return dados


cursor.close()
conn.close()

class DataPaises:
    def __init__(self, data_frame):
        self.data = data_frame

    def pegar_dados_de_pais(self, nome_país):
        nome_país = self.data[self.data['pais'] == nome_país]
        return nome_país

    def pegar_dados_de_ano(self, ano):
        data_ano = self.data[self.data['ano'] == ano]
        return data_ano

    def pegar_indicador_nomepaís_ano(self, nome_país, ano, indicador):
        resultado = self.data[(self.data['pais'] == nome_país) & (self.data['ano'] == ano)]
        if not resultado.empty:
            return resultado[indicador].values[0]
        else:
            print(f"No data found for {nome_país} in {ano}.")
            return None