# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import DataNode_pb2 as DataNode__pb2


class DataNodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.heartbeat = channel.unary_unary(
                '/DataNode.DataNode/heartbeat',
                request_serializer=DataNode__pb2.msg.SerializeToString,
                response_deserializer=DataNode__pb2.msg.FromString,
                )
        self.upload = channel.stream_unary(
                '/DataNode.DataNode/upload',
                request_serializer=DataNode__pb2.uploadFile.SerializeToString,
                response_deserializer=DataNode__pb2.msg.FromString,
                )
        self.replica = channel.stream_unary(
                '/DataNode.DataNode/replica',
                request_serializer=DataNode__pb2.uploadFile.SerializeToString,
                response_deserializer=DataNode__pb2.msg.FromString,
                )
        self.get = channel.unary_stream(
                '/DataNode.DataNode/get',
                request_serializer=DataNode__pb2.msg.SerializeToString,
                response_deserializer=DataNode__pb2.saveFile.FromString,
                )
        self.remove = channel.unary_unary(
                '/DataNode.DataNode/remove',
                request_serializer=DataNode__pb2.msg.SerializeToString,
                response_deserializer=DataNode__pb2.msg.FromString,
                )


class DataNodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def heartbeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upload(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def replica(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'heartbeat': grpc.unary_unary_rpc_method_handler(
                    servicer.heartbeat,
                    request_deserializer=DataNode__pb2.msg.FromString,
                    response_serializer=DataNode__pb2.msg.SerializeToString,
            ),
            'upload': grpc.stream_unary_rpc_method_handler(
                    servicer.upload,
                    request_deserializer=DataNode__pb2.uploadFile.FromString,
                    response_serializer=DataNode__pb2.msg.SerializeToString,
            ),
            'replica': grpc.stream_unary_rpc_method_handler(
                    servicer.replica,
                    request_deserializer=DataNode__pb2.uploadFile.FromString,
                    response_serializer=DataNode__pb2.msg.SerializeToString,
            ),
            'get': grpc.unary_stream_rpc_method_handler(
                    servicer.get,
                    request_deserializer=DataNode__pb2.msg.FromString,
                    response_serializer=DataNode__pb2.saveFile.SerializeToString,
            ),
            'remove': grpc.unary_unary_rpc_method_handler(
                    servicer.remove,
                    request_deserializer=DataNode__pb2.msg.FromString,
                    response_serializer=DataNode__pb2.msg.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataNode.DataNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataNode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def heartbeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNode.DataNode/heartbeat',
            DataNode__pb2.msg.SerializeToString,
            DataNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upload(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/DataNode.DataNode/upload',
            DataNode__pb2.uploadFile.SerializeToString,
            DataNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def replica(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/DataNode.DataNode/replica',
            DataNode__pb2.uploadFile.SerializeToString,
            DataNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/DataNode.DataNode/get',
            DataNode__pb2.msg.SerializeToString,
            DataNode__pb2.saveFile.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def remove(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataNode.DataNode/remove',
            DataNode__pb2.msg.SerializeToString,
            DataNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
