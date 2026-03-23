from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient

from airflow import DAG
from airflow.operators.python import PythonOperator

POSTGRES_URI = "postgresql+psycopg2://etl_user:etl_pass@postgres:5432/etl_lab"
MONGO_URI = "mongodb://admin:admin123@mongodb:27017/"

def gerar_estatisticas():
    engine = create_engine(POSTGRES_URI)

    df = pd.read_sql("SELECT * FROM aula.alunos_tratados", engine)

    total_validos = int(len(df))
    media_nota = float(df["nota"].mean()) if not df.empty else 0.0

    por_curso = {}
    por_classificacao = {}

    if not df.empty:
        por_curso = df["curso"].value_counts().to_dict()
        por_classificacao = df["classificacao"].value_counts().to_dict()

    client = MongoClient(MONGO_URI)
    db = client["etl_stats"]
    collection = db["resumo_execucoes"]

    documento = {
        "pipeline": "etl_alunos",
        "data_execucao": datetime.utcnow(),
        "total_validos": total_validos,
        "media_nota": media_nota,
        "por_curso": por_curso,
        "por_classificacao": por_classificacao
    }

    collection.insert_one(documento)
    client.close()

with DAG(
    dag_id="estatisticas_mongodb",
    start_date=datetime(2026, 3, 1),
    schedule=None,
    catchup=False,
    tags=["nosql", "mongodb", "aula"],
) as dag:

    t1 = PythonOperator(
        task_id="gerar_estatisticas_mongodb",
        python_callable=gerar_estatisticas
    )