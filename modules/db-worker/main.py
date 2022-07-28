from kafka import KafkaConsumer
import json
from db import get_person, load_person
import logging
import sys

logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

consumer_persons = KafkaConsumer(bootstrap_servers = ['kafka:9092'],
value_deserializer = lambda m: json.dumps(m.decode('utf-8')))
consumer_persons.subscribe(topics='persons')

for message in consumer_persons:
    print(message)

# for message in consumer_persons:
#     try:
#         logging.debug('attempting to retrieve record')
#         get_person(message.person_id)
#         logging.debug('record found, no need for a write')
#     except:
#         load_person(message)
#         logging.debug('wrote record to db')
