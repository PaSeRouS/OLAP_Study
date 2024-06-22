from confluent_kafka import Producer
import json

config = {
    'bootstrap.servers': 'localhost:9093',  # адрес Kafka сервера
    'client.id': 'simple-producer',
    'sasl.mechanism':'PLAIN',
    'security.protocol': 'SASL_PLAINTEXT',
    'sasl.username': 'admin',
    'sasl.password': 'admin-secret'
}

producer = Producer(**config)

def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

def send_message(data):
    try:
        # Асинхронная отправка сообщения
        producer.produce('LostReason', data.encode('utf-8'), callback=delivery_report)
        producer.poll(0)  # Поллинг для обработки обратных вызовов
    except BufferError:
        print(f"Local producer queue is full ({len(producer)} messages awaiting delivery): try again")

def main():
    from Connect_DB import connect_CH

    client = connect_CH()

    data = client.execute('select * from dict_LostReason')

    for row in data:
        json_data = json.dumps(
            {
                'lostreason_id': row[0],
                'lost_name': row[1]
            }
        )

        send_message(json_data)
        producer.flush()

if __name__ == '__main__':
    main()
