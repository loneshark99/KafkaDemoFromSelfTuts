import json
import time

from kafka import KafkaProducer
from data import get_registered_user


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


def get_partition(key, all, available):
    return


producer = KafkaProducer(bootstrap_servers=['192.168.86.32:9092'],
                         value_serializer=json_serializer)
if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("registered_user", registered_user)
        time.sleep(4)
