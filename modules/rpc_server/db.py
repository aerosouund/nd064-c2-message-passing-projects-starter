import psycopg2
from shapely import wkt
from shapely.geometry import Point
import os

def connect():
    conn = psycopg2.connect(
        host=os.environ['DB_HOST'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD'])
    return conn
 

def get_location(location_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM location WHERE id=%s', [location_id])
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results[0]
    

def load_location(location):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO location (id, person_id, coordinate, creation_time) VALUES (%s, %s, %s, %s)',
        (location['id'], location['person_id'], wkt.dumps(Point(location["latitude"], location["longitude"])), location['created_at'])
        )
    conn.commit()
    cursor.close()
    conn.close()
    