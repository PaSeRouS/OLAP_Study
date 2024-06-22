from clickhouse_driver import Client
import json
import time


def openKeyfile():
    with open("./secrets.json") as json_file:
        param_сonnect = json.load(json_file)

    return param_сonnect


def connect_CH(np=True, server='ch', schema='default', port=9000):
    param_сonnect = openKeyfile()

    for _ in range(7):
        try:
            client = Client(param_сonnect['server'][0]['host'],
                            user=param_сonnect['server'][0]['user'],
                            password=param_сonnect['server'][0]['password'],
                            port=param_сonnect['server'][0]['port'],
                            verify=False,
                            database='',
                            settings={"numpy_columns": True, 'use_numpy': True},
                            compression=True)
            return client
        except Exception as e:
            print(e, "Нет коннекта к КликХаус")
            time.sleep(60)

