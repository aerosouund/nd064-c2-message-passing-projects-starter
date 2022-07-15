from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from appزservices import LocationService

app = Flask(__name__)

db = SQLAlchemy()



@app.route('/api/locations/<location_id>')
def get_locations(methods=['GET']):
    location = 'loc'
    return jsonify(location)




