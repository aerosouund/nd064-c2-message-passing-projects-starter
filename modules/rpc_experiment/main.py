import grpc
import locations_pb2
import locations_pb2_grpc

print("Sending payload...")

channel = grpc.insecure_channel("udaconnect-locations:5005")
stub = locations_pb2_grpc.LocationServiceStub(channel)

location = locations_pb2.LocationMessage(
    id="2222",
    person_id="USER123",
    created_at='2020-03-12',
    longitude=2.5,
    latitude=3.5
)


response = stub.Create(location)
