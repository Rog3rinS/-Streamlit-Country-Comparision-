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
