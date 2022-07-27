from kafka import KafkaConsumer
import json

from .services import PersonService

consumer_persons = KafkaConsumer('persons', bootstrap_servers = ['kafka:9092'],
value_deserializer = lambda m: json.loads(m.decode('utf-8')))

for message in consumer_persons:
    try:
        PersonService.retrieve(message.person_id)
    except:
        PersonService.create(message)
