from flask import Flask, jsonify
from app.services import LocationService
from flask_accepts import accepts, responds

app = Flask(__name__)



@app.route('/api/locations/<person_id>')
def get_persons(person_id, methods=['GET']):
    location = LocationService.retrieve(person_id)
    return jsonify(location)
