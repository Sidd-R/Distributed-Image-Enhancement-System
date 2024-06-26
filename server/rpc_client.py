#  grpc client implementation
import logging
import grpc
from protos import math_pb2_grpc
from protos import math_pb2
from protos import image_enhance_pb2_grpc
from protos import image_enhance_pb2
import threading
from PIL import Image
import io
import datetime
import sys
import time

logging.basicConfig(
    filename="./logs/main_server.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


# def run(num1, num2):
#     with grpc.insecure_channel("localhost:50051") as channel:
#         stub = math_pb2_grpc.MathServiceStub(channel)
#         request = math_pb2.MathRequest(a=num1, b=num2)

#         logging.info(f"rpc requests sent for {num1} and {num2}")
        
#         result = []
        
#         def thread_wrapper(func, request, name, result):
#             print(f"{name} thread started\n")
#             logging.info(f"{name} thread started")
#             response = func(request)
#             print(f"In {name} thread response is {response.result} for {request.a} and {request.b}\n")
#             logging.info(f"In {name} thread response is {response.result} for {request.a} and {request.b}")
#             # print(f"{name} thread completed\n")
#             result.append(response.result)
            
        
#         add_thread = threading.Thread(target=thread_wrapper, args=(stub.Addition, request, "add",result))
#         sub_thread = threading.Thread(target=thread_wrapper, args=(stub.Substraction, request, "sub",result))
#         mul_thread = threading.Thread(target=thread_wrapper, args=(stub.Multiplication, request, "mul",result))
#         div_thread = threading.Thread(target=thread_wrapper, args=(stub.Division, request, "div",result))
#         pow_thread = threading.Thread(target=thread_wrapper, args=(stub.Power, request, "pow",result))

#         # add_response = stub.Addition(request)
#         # sub_response = stub.Substraction(request)
#         # mul_response = stub.Multiplication(request)
#         # div_response = stub.Division(request)        
#         # pow_response = stub.Power(request)
        
#         add_thread.start()
#         sub_thread.start()
#         mul_thread.start()
#         div_thread.start()
#         pow_thread.start()
        
#         add_thread.join()
#         sub_thread.join()
#         mul_thread.join()
#         div_thread.join()
#         pow_thread.join()
        
        
                

#         logging.info(f"rpc requests completed for {num1} and {num2}")
#     # return [
#     #     add_response.result,
#     #     sub_response.result,
#     #     mul_response.result,
#     #     div_response.result,
#     #     pow_response.result,
#     # ]
    
#     # print(f"result is {result}")
    
#     return result

class RpcClient:
    def __init__(self) -> None:
        self.id = 22

    def enhance_image(self,image_path="./temp/wumpus.jpeg",port=50051):
        # image_path = "./temp/wumpus.jpeg"
        with open(image_path, "rb") as f:
            image_data = f.read()
            
            with grpc.insecure_channel(f"localhost:{port}") as channel:
                stub = image_enhance_pb2_grpc.ImageEnhancerStub(channel)
                request = image_enhance_pb2.ImageRequest(id="1", image_data=image_data)
                response = stub.EnhanceImage(request)
                image = Image.open(io.BytesIO(response.image_data))
                
                # save image in processed_image folder with current timestamp
                filename = f"processed_image_{round(time.time())}.jpeg"
                processed_img_path = f"./temp/{filename}"
                image.save(processed_img_path)    
                
                return filename

if __name__ == "__main__":
    client = RpcClient()
    
    while input("Do you want to enhance image? (y/n): ") == "y":
        client.enhance_image()