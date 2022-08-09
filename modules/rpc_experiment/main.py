import grpc
import locations_pb2
import locations_pb2_grpc

print("Sending payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = locations_pb2_grpc.LocationServiceStub(channel)

response = stub.Get(locations_pb2.LocationMessage())
print(response)
