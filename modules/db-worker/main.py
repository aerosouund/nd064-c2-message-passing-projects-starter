from kafka import KafkaConsumer
import json
from .db import get_person, load_person 

consumer_persons = KafkaConsumer('persons', bootstrap_servers = ['kafka:9092'],
value_deserializer = lambda m: json.loads(m.decode('utf-8')))

for message in consumer_persons:
    try:
        get_person(message.person_id)
    except:
        load_person(message)
