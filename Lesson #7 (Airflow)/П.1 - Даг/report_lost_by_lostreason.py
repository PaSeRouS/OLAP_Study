from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta

default_args = {
    "owner": "Serov",
    "start_date": datetime(2024, 7, 31),
    "retries": 1,
    "retry_delay": timedelta(seconds=60),
}

dag = DAG(
    dag_id="report_lost_by_lostreason",
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    max_active_runs=1
)


def main():
    import json
    import psycopg2
    from clickhouse_driver import Client

    with open('/opt/airflow/dags/keys/secrets.json') as json_file:
        param_сonnect = json.load(json_file)

    client_CH = Client(
        param_сonnect['clickhouse'][0]['host'],
        user=param_сonnect['clickhouse'][0]['user'],
        password=param_сonnect['clickhouse'][0]['password'],
        port=param_сonnect['clickhouse'][0]['port'],
        verify=False,
        compression=True
    )

    client_PG = psycopg2.connect(
        host=param_сonnect['postgres'][0]['host'],
        user=param_сonnect['postgres'][0]['user'],
        password=param_сonnect['postgres'][0]['password'],
        port=param_сonnect['postgres'][0]['port'],
        database=param_сonnect['postgres'][0]['database']
    )

    client_CH.execute(f"""
        INSERT INTO report.lost_by_lostreason
        select lostreason_id
             , count(shk_id) qty_lost
             , sum(amount) sum_lost
        from Shk_LostPost
        group by lostreason_id
    """)

    print('Вставка данных в витрину report.lost_by_lostreason в clickhouse')

    df = client_CH.query_dataframe(f"""
        select lostreason_id
             , qty_lost
             , sum_lost
        from report.lost_by_lostreason final
    """)

    df = df.to_json(orient='records', date_format='iso')

    cursor = client_PG.cursor()
    cursor.execute(f"CALL sync.lost_by_lostreason_import(_src := '{df}')")
    client_PG.commit()

    print('Вставка данных в витрину report.lost_by_lostreason в postgres')

    cursor.close()
    client_PG.close()

    client_CH.disconnect()


task1 = PythonOperator(
    task_id="report_lost_by_lostreason",
    python_callable=main,
    dag=dag
)
