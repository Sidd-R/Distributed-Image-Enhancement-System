# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import math_pb2 as math__pb2


class MathServiceStub(object):
    """The math service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Addition = channel.unary_unary(
                '/trial.MathService/Addition',
                request_serializer=math__pb2.MathRequest.SerializeToString,
                response_deserializer=math__pb2.MathResponse.FromString,
                )
        self.Substraction = channel.unary_unary(
                '/trial.MathService/Substraction',
                request_serializer=math__pb2.MathRequest.SerializeToString,
                response_deserializer=math__pb2.MathResponse.FromString,
                )
        self.Multiplication = channel.unary_unary(
                '/trial.MathService/Multiplication',
                request_serializer=math__pb2.MathRequest.SerializeToString,
                response_deserializer=math__pb2.MathResponse.FromString,
                )
        self.Division = channel.unary_unary(
                '/trial.MathService/Division',
                request_serializer=math__pb2.MathRequest.SerializeToString,
                response_deserializer=math__pb2.MathResponse.FromString,
                )
        self.Power = channel.unary_unary(
                '/trial.MathService/Power',
                request_serializer=math__pb2.MathRequest.SerializeToString,
                response_deserializer=math__pb2.MathResponse.FromString,
                )


class MathServiceServicer(object):
    """The math service definition.
    """

    def Addition(self, request, context):
        """adds two numbers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Substraction(self, request, context):
        """subtracts two numbers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Multiplication(self, request, context):
        """multiplies two numbers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Division(self, request, context):
        """divides two numbers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Power(self, request, context):
        """power of two numbers
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MathServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Addition': grpc.unary_unary_rpc_method_handler(
                    servicer.Addition,
                    request_deserializer=math__pb2.MathRequest.FromString,
                    response_serializer=math__pb2.MathResponse.SerializeToString,
            ),
            'Substraction': grpc.unary_unary_rpc_method_handler(
                    servicer.Substraction,
                    request_deserializer=math__pb2.MathRequest.FromString,
                    response_serializer=math__pb2.MathResponse.SerializeToString,
            ),
            'Multiplication': grpc.unary_unary_rpc_method_handler(
                    servicer.Multiplication,
                    request_deserializer=math__pb2.MathRequest.FromString,
                    response_serializer=math__pb2.MathResponse.SerializeToString,
            ),
            'Division': grpc.unary_unary_rpc_method_handler(
                    servicer.Division,
                    request_deserializer=math__pb2.MathRequest.FromString,
                    response_serializer=math__pb2.MathResponse.SerializeToString,
            ),
            'Power': grpc.unary_unary_rpc_method_handler(
                    servicer.Power,
                    request_deserializer=math__pb2.MathRequest.FromString,
                    response_serializer=math__pb2.MathResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'trial.MathService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MathService(object):
    """The math service definition.
    """

    @staticmethod
    def Addition(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trial.MathService/Addition',
            math__pb2.MathRequest.SerializeToString,
            math__pb2.MathResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Substraction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trial.MathService/Substraction',
            math__pb2.MathRequest.SerializeToString,
            math__pb2.MathResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Multiplication(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trial.MathService/Multiplication',
            math__pb2.MathRequest.SerializeToString,
            math__pb2.MathResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Division(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trial.MathService/Division',
            math__pb2.MathRequest.SerializeToString,
            math__pb2.MathResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Power(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/trial.MathService/Power',
            math__pb2.MathRequest.SerializeToString,
            math__pb2.MathResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)