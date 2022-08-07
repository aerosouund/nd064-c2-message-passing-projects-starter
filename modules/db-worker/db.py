import psycopg2
from typing import Dict
import os

def connect():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    return conn
 

def get_person(person_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT id FROM person WHERE id=%s', [person_id])
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results[0]
    

def load_person(person: Dict):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO person (id, first_name, laft_name, company_name) VALUES (%s, %s, %s, %s)',
        (person.id, person.first_name, person.last_name, person.company_name)
        )
    conn.commit()
    cursor.close()
    conn.close()
    