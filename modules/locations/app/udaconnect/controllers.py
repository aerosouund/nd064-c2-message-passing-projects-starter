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
import app.udaconnect.locations_pb2 as locations_pb2
import app.udaconnect.locations_pb2_grpc as locations_pb2_grpc
import grpc
import time
from concurrent import futures

DATE_FORMAT = "%Y-%m-%d"

api = Namespace("UdaConnect", description="Connections via geolocation.")  # noqa


# TODO: This needs better exception handling


@api.route("/locations")
@api.route("/locations/<location_id>")
@api.param("location_id", "Unique ID for a given Location", _in="query")
class LocationResource(Resource):
    @accepts(schema=LocationSchema)
    @responds(schema=LocationSchema)
    def post(self) -> Location:
        request.get_json()
        location: Location = LocationService.create(request.get_json())
        return location

    @responds(schema=LocationSchema)
    def get(self, location_id) -> Location:
        location: Location = LocationService.retrieve(location_id)
        return location


class LocationServicer(locations_pb2_grpc.LocationServiceServicer):
    def Get(self, request, context):
        location: Location = LocationService.retrieve(request.id)
        result = locations_pb2.LocationMessage(location)
        return result

    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "created_at": request.created_at,
            "longitude": request.longitude,
            "latitude": request.latitude
        }
        print(request_value)
        # replace with kafka queue write
        location: Location = LocationService.create(request_value.get_json())

        return locations_pb2.LocationMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
locations_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)


print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)



