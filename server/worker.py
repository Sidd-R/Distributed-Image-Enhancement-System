# implement grpc server logic
import sys
import numpy as np
import tensorflow as tf
from protos import image_enhance_pb2
from protos import image_enhance_pb2_grpc
from keras.preprocessing.image import img_to_array
# import os.path
# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from concurrent import futures
import logging
import grpc
from protos import math_pb2
from protos import math_pb2_grpc


class RPCService(math_pb2_grpc.MathServiceServicer, image_enhance_pb2_grpc.ImageProcessorServiceServicer):
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
    
    def SplitImage(self, request, context):
        # Convert the received bytes to a numpy array
        img_rgb = np.frombuffer(request.image_data, dtype=np.uint8).reshape(request.image_height, request.image_width,  3)
        
        def split_img(img_rgb):
            img_normalized = img_rgb /  255.0
            img_keras = img_to_array(img_normalized)
            img_keras = np.expand_dims(img_keras, axis=0)
            patch_size = (img_rgb.shape[0]//8,  img_rgb.shape[1]//8)

            patches = tf.image.extract_patches(
                images=img_keras,
                sizes=[1, *patch_size,  1],
                strides=[1, patch_size[0], patch_size[1],  1],
                rates=[1,  1,  1,  1],
                padding='VALID',
            )
            patches = tf.reshape(patches, (64, img_rgb.shape[0]//8, img_rgb.shape[1]//8, 3))
            return patches
        # Call the split_img function
        patches = split_img(img_rgb)
        
        # Serialize the patches to send them back
        serialized_patches = [patch.tobytes() for patch in patches]
        
        # Return the patches
        return image_enhance_pb2.ImagePatchesResponse(patches=serialized_patches)

    def MergePatches(self, request, context):
        # Deserialize the patches from the received bytes
        patches = [np.frombuffer(patch, dtype=np.float32).reshape(request.image_height//8, request.image_width//8,  3) for patch in request.patches]
        
        def merge_patches(patches, img_shape):
            # Determine the dimensions of the resulting image
            height, width, _ = img_shape
            patch_height, patch_width = patches.shape[1], patches.shape[2]

            # Initialize an empty image with the same shape as the original image
            merged_image = np.zeros(img_shape, dtype=np.float32)

            # Loop through the patches and place them back into the original image
            for i in range(height//patch_height):
                start_row = i * patch_height
                end_row = start_row + patch_height
                for j in range(width//patch_width):
                    start_col = j * patch_width
                    end_col = start_col + patch_width
                    merged_image[start_row:end_row, start_col:end_col] = patches[i*height//patch_height+j]

            # Normalize the values back to [0,  255] range
            merged_image = merged_image*255
            merged_image = tf.cast(merged_image, tf.uint8)

            return merged_image.numpy()

        # Call the merge_patches function
        merged_image = merge_patches(patches, (request.image_height, request.image_width,  3))
        
        # Serialize the merged image to send it back
        serialized_image = merged_image.tobytes()
        
        # Return the merged image
        return image_enhance_pb2.MergedImageResponse(merged_image=serialized_image)



def serve():
    PORT = sys.argv[1] if sys.argv[1:] else "50051"
    
    id = sys.argv[2] if sys.argv[2:] else "1"

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    math_pb2_grpc.add_MathServiceServicer_to_server(RPCService(), server)
    image_enhance_pb2_grpc.add_ImageProcessorServiceServicer_to_server(RPCService(), server)
    server.add_insecure_port("[::]:" + PORT)
    server.start()
    print("Worker server is running on port: " + PORT)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
