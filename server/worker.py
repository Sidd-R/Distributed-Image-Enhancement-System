# implement grpc server logic
import sys

# import os.path
# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from concurrent import futures
import logging
import grpc
from protos import math_pb2
from protos import math_pb2_grpc


class RPCService(math_pb2_grpc.MathServiceServicer):
    def Addition(self, request, context):
        logging.info(f"add request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a + request.b)
        return response

    def Substraction(self, request, context):
        logging.info(f"sub request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a - request.b)
        return response

    def Multiplication(self, request, context):
        logging.info(f"mul request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a * request.b)
        return response

    def Division(self, request, context):
        logging.info(f"div request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a / request.b)
        return response

    def Power(self, request, context):
        logging.info(f"pow request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a**request.b)
        return response


def serve():
    PORT = sys.argv[1] if sys.argv[1:] else "50051"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    math_pb2_grpc.add_MathServiceServicer_to_server(RPCService(), server)
    server.add_insecure_port("[::]:" + PORT)
    server.start()
    print("server is running on port: " + PORT)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
