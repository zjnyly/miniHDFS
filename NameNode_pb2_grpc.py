# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import NameNode_pb2 as NameNode__pb2


class NameNodeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.checkNameNodeStatus = channel.unary_unary(
                '/NameNode.NameNode/checkNameNodeStatus',
                request_serializer=NameNode__pb2.msg.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.bindClient = channel.unary_unary(
                '/NameNode.NameNode/bindClient',
                request_serializer=NameNode__pb2.userInfo.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.register = channel.unary_unary(
                '/NameNode.NameNode/register',
                request_serializer=NameNode__pb2.userInfo.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.pwd = channel.unary_unary(
                '/NameNode.NameNode/pwd',
                request_serializer=NameNode__pb2.msg.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.mkdir = channel.unary_unary(
                '/NameNode.NameNode/mkdir',
                request_serializer=NameNode__pb2.msg.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.cd = channel.unary_unary(
                '/NameNode.NameNode/cd',
                request_serializer=NameNode__pb2.msg.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.upload = channel.unary_unary(
                '/NameNode.NameNode/upload',
                request_serializer=NameNode__pb2.fileInfo.SerializeToString,
                response_deserializer=NameNode__pb2.instructions.FromString,
                )
        self.delete = channel.unary_unary(
                '/NameNode.NameNode/delete',
                request_serializer=NameNode__pb2.fileInfo.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.error = channel.unary_unary(
                '/NameNode.NameNode/error',
                request_serializer=NameNode__pb2.msg.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.download = channel.unary_unary(
                '/NameNode.NameNode/download',
                request_serializer=NameNode__pb2.fileInfo.SerializeToString,
                response_deserializer=NameNode__pb2.instructions.FromString,
                )
        self.readfile = channel.unary_unary(
                '/NameNode.NameNode/readfile',
                request_serializer=NameNode__pb2.fileInfo.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.releasefile = channel.unary_unary(
                '/NameNode.NameNode/releasefile',
                request_serializer=NameNode__pb2.fileInfo.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.ls = channel.unary_unary(
                '/NameNode.NameNode/ls',
                request_serializer=NameNode__pb2.msg.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.cp = channel.unary_unary(
                '/NameNode.NameNode/cp',
                request_serializer=NameNode__pb2.cpMsg.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )
        self.join = channel.unary_unary(
                '/NameNode.NameNode/join',
                request_serializer=NameNode__pb2.dataNodeInfo.SerializeToString,
                response_deserializer=NameNode__pb2.msg.FromString,
                )


class NameNodeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def checkNameNodeStatus(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def bindClient(self, request, context):
        """for Client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pwd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def mkdir(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cd(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def upload(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def error(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def download(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def readfile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def releasefile(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ls(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def cp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def join(self, request, context):
        """for DataNode
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NameNodeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'checkNameNodeStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.checkNameNodeStatus,
                    request_deserializer=NameNode__pb2.msg.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'bindClient': grpc.unary_unary_rpc_method_handler(
                    servicer.bindClient,
                    request_deserializer=NameNode__pb2.userInfo.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'register': grpc.unary_unary_rpc_method_handler(
                    servicer.register,
                    request_deserializer=NameNode__pb2.userInfo.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'pwd': grpc.unary_unary_rpc_method_handler(
                    servicer.pwd,
                    request_deserializer=NameNode__pb2.msg.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'mkdir': grpc.unary_unary_rpc_method_handler(
                    servicer.mkdir,
                    request_deserializer=NameNode__pb2.msg.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'cd': grpc.unary_unary_rpc_method_handler(
                    servicer.cd,
                    request_deserializer=NameNode__pb2.msg.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'upload': grpc.unary_unary_rpc_method_handler(
                    servicer.upload,
                    request_deserializer=NameNode__pb2.fileInfo.FromString,
                    response_serializer=NameNode__pb2.instructions.SerializeToString,
            ),
            'delete': grpc.unary_unary_rpc_method_handler(
                    servicer.delete,
                    request_deserializer=NameNode__pb2.fileInfo.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'error': grpc.unary_unary_rpc_method_handler(
                    servicer.error,
                    request_deserializer=NameNode__pb2.msg.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'download': grpc.unary_unary_rpc_method_handler(
                    servicer.download,
                    request_deserializer=NameNode__pb2.fileInfo.FromString,
                    response_serializer=NameNode__pb2.instructions.SerializeToString,
            ),
            'readfile': grpc.unary_unary_rpc_method_handler(
                    servicer.readfile,
                    request_deserializer=NameNode__pb2.fileInfo.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'releasefile': grpc.unary_unary_rpc_method_handler(
                    servicer.releasefile,
                    request_deserializer=NameNode__pb2.fileInfo.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'ls': grpc.unary_unary_rpc_method_handler(
                    servicer.ls,
                    request_deserializer=NameNode__pb2.msg.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'cp': grpc.unary_unary_rpc_method_handler(
                    servicer.cp,
                    request_deserializer=NameNode__pb2.cpMsg.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
            'join': grpc.unary_unary_rpc_method_handler(
                    servicer.join,
                    request_deserializer=NameNode__pb2.dataNodeInfo.FromString,
                    response_serializer=NameNode__pb2.msg.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'NameNode.NameNode', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class NameNode(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def checkNameNodeStatus(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/checkNameNodeStatus',
            NameNode__pb2.msg.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def bindClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/bindClient',
            NameNode__pb2.userInfo.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/register',
            NameNode__pb2.userInfo.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def pwd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/pwd',
            NameNode__pb2.msg.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def mkdir(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/mkdir',
            NameNode__pb2.msg.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cd(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/cd',
            NameNode__pb2.msg.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def upload(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/upload',
            NameNode__pb2.fileInfo.SerializeToString,
            NameNode__pb2.instructions.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/delete',
            NameNode__pb2.fileInfo.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def error(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/error',
            NameNode__pb2.msg.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def download(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/download',
            NameNode__pb2.fileInfo.SerializeToString,
            NameNode__pb2.instructions.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def readfile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/readfile',
            NameNode__pb2.fileInfo.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def releasefile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/releasefile',
            NameNode__pb2.fileInfo.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ls(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/ls',
            NameNode__pb2.msg.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def cp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/cp',
            NameNode__pb2.cpMsg.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def join(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/NameNode.NameNode/join',
            NameNode__pb2.dataNodeInfo.SerializeToString,
            NameNode__pb2.msg.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
