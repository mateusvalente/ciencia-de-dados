from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine, text

from airflow import DAG
from airflow.operators.python import PythonOperator

DB_URI = "postgresql+psycopg2://etl_user:etl_pass@postgres:5432/etl_lab"

def extrair_do_banco():
    engine = create_engine(DB_URI)
    df = pd.read_sql("SELECT id, nome, curso, idade, email, nota FROM aula.alunos_raw", engine)
    df.to_csv("/opt/airflow/data/out/alunos_extraidos.csv", index=False)

def transformar_validar():
    df = pd.read_csv("/opt/airflow/data/out/alunos_extraidos.csv")

    invalidos = []
    validos = []

    for _, row in df.iterrows():
        motivo = []

        nome = row.get("nome")
        email = row.get("email")
        idade = row.get("idade")
        nota = row.get("nota")

        if pd.isna(nome) or str(nome).strip() == "":
            motivo.append("nome vazio")

        if pd.isna(email) or "@" not in str(email) or "." not in str(email):
            motivo.append("email inválido")

        try:
            idade_num = int(idade)
            if idade_num < 18:
                motivo.append("menor de idade")
        except Exception:
            motivo.append("idade inválida")

        try:
            nota_num = float(nota)
        except Exception:
            motivo.append("nota inválida")
            nota_num = None

        registro = row.to_dict()

        if motivo:
            registro["motivo_erro"] = "; ".join(motivo)
            invalidos.append(registro)
        else:
            if nota_num >= 8:
                classificacao = "Excelente"
            elif nota_num >= 6:
                classificacao = "Regular"
            else:
                classificacao = "Risco"

            registro["nota"] = nota_num
            registro["status_validacao"] = "valido"
            registro["classificacao"] = classificacao
            validos.append(registro)

    pd.DataFrame(validos).to_csv("/opt/airflow/data/out/alunos_validos.csv", index=False)
    pd.DataFrame(invalidos).to_csv("/opt/airflow/data/out/alunos_invalidos.csv", index=False)

def carregar_no_banco():
    engine = create_engine(DB_URI)

    df_validos = pd.read_csv("/opt/airflow/data/out/alunos_validos.csv")
    df_invalidos = pd.read_csv("/opt/airflow/data/out/alunos_invalidos.csv")

    with engine.begin() as conn:
        conn.execute(text("TRUNCATE TABLE aula.alunos_tratados"))
        conn.execute(text("TRUNCATE TABLE aula.alunos_invalidos"))

    if not df_validos.empty:
        df_validos[["id","nome","curso","idade","email","nota","status_validacao","classificacao"]].to_sql(
            "alunos_tratados",
            engine,
            schema="aula",
            if_exists="append",
            index=False
        )

    if not df_invalidos.empty:
        cols = ["id","nome","curso","idade","email","nota","motivo_erro"]
        for c in cols:
            if c not in df_invalidos.columns:
                df_invalidos[c] = None

        df_invalidos[cols].to_sql(
            "alunos_invalidos",
            engine,
            schema="aula",
            if_exists="append",
            index=False
        )

def gerar_relatorio():
    engine = create_engine(DB_URI)
    with engine.connect() as conn:
        total_raw = conn.execute(text("SELECT COUNT(*) FROM aula.alunos_raw")).scalar()
        total_validos = conn.execute(text("SELECT COUNT(*) FROM aula.alunos_tratados")).scalar()
        total_invalidos = conn.execute(text("SELECT COUNT(*) FROM aula.alunos_invalidos")).scalar()

    with open("/opt/airflow/data/out/relatorio_etl.txt", "w", encoding="utf-8") as f:
        f.write("RELATÓRIO ETL\n")
        f.write(f"Total bruto: {total_raw}\n")
        f.write(f"Total válidos: {total_validos}\n")
        f.write(f"Total inválidos: {total_invalidos}\n")

with DAG(
    dag_id="etl_alunos",
    start_date=datetime(2026, 3, 1),
    schedule=None,
    catchup=False,
    tags=["etl", "aula"],
) as dag:

    t1 = PythonOperator(
        task_id="extrair_do_banco",
        python_callable=extrair_do_banco
    )

    t2 = PythonOperator(
        task_id="transformar_validar",
        python_callable=transformar_validar
    )

    t3 = PythonOperator(
        task_id="carregar_no_banco",
        python_callable=carregar_no_banco
    )

    t4 = PythonOperator(
        task_id="gerar_relatorio",
        python_callable=gerar_relatorio
    )

    t1 >> t2 >> t3 >> t4