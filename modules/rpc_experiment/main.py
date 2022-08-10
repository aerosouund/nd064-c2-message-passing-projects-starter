import grpc
import locations_pb2
import locations_pb2_grpc
from concurrent import futures
import time
import logging
from db import load_location
import sys


logging.basicConfig(
    stream=sys.stdout,
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S')

class LocationServicer(locations_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        print("Received a message!")

        request_value = {
            "id": request.id,
            "person_id": request.person_id,
            "created_at": request.created_at,
            "longitude": request.longitude,
            "latitude": request.latitude
        }
        print('creating record with value ', request_value)
        load_location(request_value)

        return locations_pb2.LocationMessage(**request_value)

def create_rpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    locations_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)
    return server


if __name__=="__main__":
    print("Server starting on port 5005...")
    server = create_rpc_server()
    server.add_insecure_port("[::]:5005")
    server.start()
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)
