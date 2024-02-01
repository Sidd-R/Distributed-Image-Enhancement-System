#  grpc client implementation
import logging

import grpc
from protos import math_pb2_grpc
from protos import math_pb2

logging.basicConfig(
    filename="./logs/main_server.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def run(num1, num2):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = math_pb2_grpc.MathServiceStub(channel)
        request = math_pb2.MathRequest(a=num1, b=num2)

        logging.info(f"rpc requests sent for {num1} and {num2}")

        add_response = stub.Addition(request)
        logging.debug(
            f"add response received for {num1} and {num2} as {add_response.result}"
        )

        sub_response = stub.Substraction(request)
        logging.debug(
            f"sub response received for {num1} and {num2} as {sub_response.result}"
        )

        mul_response = stub.Multiplication(request)
        logging.debug(
            f"mul response received for {num1} and {num2} as {mul_response.result}"
        )

        div_response = stub.Division(request)
        logging.debug(
            f"div response received for {num1} and {num2} as {div_response.result}"
        )

        pow_response = stub.Power(request)
        logging.debug(
            f"pow response received for {num1} and {num2} as {pow_response.result}"
        )

        logging.info(f"rpc requests completed for {num1} and {num2}")
    return [
        add_response.result,
        sub_response.result,
        mul_response.result,
        div_response.result,
        pow_response.result,
    ]
