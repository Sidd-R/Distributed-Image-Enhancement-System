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
from protos import image_enhance_pb2
from protos import image_enhance_pb2_grpc
import io
from PIL import Image
import threading


class RPCService(math_pb2_grpc.MathServiceServicer):
    lamport_timestamp = 0
    
    def Addition(self, request, context):
        logging.info(f"add request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a + request.b)
        print(f"add response is {response.result} for {request.a} and {request.b}")
        return response

    def Substraction(self, request, context):
        logging.info(f"sub request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a - request.b)
        print(f"sub response is {response.result} for {request.a} and {request.b}")
        return response

    def Multiplication(self, request, context):
        logging.info(f"mul request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a * request.b)
        print(f"mul response is {response.result} for {request.a} and {request.b}")
        return response

    def Division(self, request, context):
        logging.info(f"div request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a / request.b)
        print(f"div response is {response.result} for {request.a} and {request.b}")
        return response

    def Power(self, request, context):
        logging.info(f"pow request received for {request.a} and {request.b}")
        response = math_pb2.MathResponse(result=request.a**request.b)
        print(f"pow response is {response.result} for {request.a} and {request.b}")
        return response
    
class ImageEnhancerServicer(image_enhance_pb2_grpc.ImageEnhancerServicer):
    lamport_timestamp = 0
    
    def process_part(self, part, processed_parts,i):
        # print(i)
        # Convert part to black and white
        processed_part = part.convert('L')
        processed_parts.append((processed_part,i))
    
    def EnhanceImage(self, request, context):
        image_bytes = request.image_data

        # Decode the image using Pillow 
        image = Image.open(io.BytesIO(image_bytes))
        
        num_parts = 4  
        width, height = image.size
        part_height = height // num_parts
        parts = []
        for i in range(num_parts):
            part = image.crop((0, i * part_height, width, (i + 1) * part_height))
            parts.append(part)
        logging.info(f"image enhance request received for {request.id} at {self.lamport_timestamp}")
        print(f"image enhance request received for {request.id} at {self.lamport_timestamp}")

        # Process parts concurrently
        processed_parts = []
        threads = []
        for i, part in enumerate(parts):
            thread = threading.Thread(target=self.process_part, args=(part, processed_parts,i))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()
            
        processed_parts.sort(key=lambda x: x[1])

        processed_parts = [x[0] for x in processed_parts]

        # Merge processed parts
        merged_image = Image.new('RGB', (width, height))
        for i, part in enumerate(processed_parts):
            merged_image.paste(part, (0, i * part_height))

        # Convert merged image to black and white
        merged_image = merged_image.convert('L')

        # Convert merged image back to bytes
        with io.BytesIO() as output:
            merged_image.save(output, format='JPEG')
            merged_image_data = output.getvalue()
                
        self.lamport_timestamp = max(request.lamport_timestamp, self.lamport_timestamp) + 1
        logging.info(f"image enhance request completed for {request.id} at {self.lamport_timestamp}")
        print(f'image enhance request completed for {request.id} at {self.lamport_timestamp}')

        
        return image_enhance_pb2.ImageResponse(image_data=merged_image_data,id=request.id, lamport_timestamp=self.lamport_timestamp)


def serve():
    PORT = sys.argv[1] if sys.argv[1:] else "50051"
    
    id = sys.argv[2] if sys.argv[2:] else "1"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    image_enhance_pb2_grpc.add_ImageEnhancerServicer_to_server(ImageEnhancerServicer(), server)
    server.add_insecure_port("[::]:" + PORT)
    server.start()
    print("Worker server is running on port: " + PORT)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
