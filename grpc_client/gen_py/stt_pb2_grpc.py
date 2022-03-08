# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import stt_pb2 as stt__pb2


class STTStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recognize = channel.unary_unary(
                '/STT/Recognize',
                request_serializer=stt__pb2.RecognizeRequest.SerializeToString,
                response_deserializer=stt__pb2.RecognizeResponse.FromString,
                )
        self.StreamingRecognize = channel.stream_stream(
                '/STT/StreamingRecognize',
                request_serializer=stt__pb2.StreamingRecognizeRequest.SerializeToString,
                response_deserializer=stt__pb2.StreamingRecognizeResponse.FromString,
                )


class STTServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Recognize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingRecognize(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_STTServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recognize': grpc.unary_unary_rpc_method_handler(
                    servicer.Recognize,
                    request_deserializer=stt__pb2.RecognizeRequest.FromString,
                    response_serializer=stt__pb2.RecognizeResponse.SerializeToString,
            ),
            'StreamingRecognize': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingRecognize,
                    request_deserializer=stt__pb2.StreamingRecognizeRequest.FromString,
                    response_serializer=stt__pb2.StreamingRecognizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'STT', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class STT(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Recognize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/STT/Recognize',
            stt__pb2.RecognizeRequest.SerializeToString,
            stt__pb2.RecognizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingRecognize(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/STT/StreamingRecognize',
            stt__pb2.StreamingRecognizeRequest.SerializeToString,
            stt__pb2.StreamingRecognizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
