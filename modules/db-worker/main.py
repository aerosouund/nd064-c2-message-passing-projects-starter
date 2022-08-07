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
    payload = json.loads(message.value)[0]
    logging.debug('attempting to retrieve record')
    try:
        print('figuring out types', payload , type(payload))
        get_person(payload['id'])
        logging.debug('record found, no need for a write')
    except:
        load_person(payload)
        logging.debug('wrote record to db')

    