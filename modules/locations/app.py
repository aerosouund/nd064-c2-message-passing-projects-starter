from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from app.services import LocationService
from flask_accepts import accepts, responds

app = Flask(__name__)

db = SQLAlchemy()



@app.route('/api/locations/<location_id>')
def get_locations(location_id, methods=['GET']):
    location = LocationService.retrieve(location_id)
    return jsonify(location)




