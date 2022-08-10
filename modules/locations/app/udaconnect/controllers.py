from datetime import datetime

from app.udaconnect.models import Location
from app.udaconnect.schemas import (
    LocationSchema
)
from app.udaconnect.services import LocationService
from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from typing import Optional, List
import app.udaconnect.locations_pb2_grpc as locations_pb2_grpc
import grpc
import logging


DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa



@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    def post(self) -> Location:
        location = request.get_json()
        logging.debug(f'the object received is {type(location)}, {location}')
        channel = grpc.insecure_channel("rpc-server:5005")
        stub = locations_pb2_grpc.LocationServiceStub(channel)
        response = stub.Create(location)
        return response

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location



