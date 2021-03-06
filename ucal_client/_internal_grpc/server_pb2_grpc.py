# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
# pylint: disable-all
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ucal_client._internal_grpc import server_pb2 as server__pb2


class ServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetConfig = channel.unary_unary(
        '/Server/GetConfig',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=server__pb2.JsonMsg.FromString,
        )
    self.GetPlan = channel.unary_stream(
        '/Server/GetPlan',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=server__pb2.BlockMsg.FromString,
        )
    self.GetData = channel.unary_stream(
        '/Server/GetData',
        request_serializer=server__pb2.TimeStampMsg.SerializeToString,
        response_deserializer=server__pb2.FrameMsg.FromString,
        )
    self.GetState = channel.unary_unary(
        '/Server/GetState',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=server__pb2.StateMsg.FromString,
        )
    self.SetPlan = channel.stream_unary(
        '/Server/SetPlan',
        request_serializer=server__pb2.BlockMsg.SerializeToString,
        response_deserializer=server__pb2.OkMsg.FromString,
        )
    self.SetConfig = channel.unary_unary(
        '/Server/SetConfig',
        request_serializer=server__pb2.JsonMsg.SerializeToString,
        response_deserializer=server__pb2.OkMsg.FromString,
        )
    self.RunNext = channel.unary_unary(
        '/Server/RunNext',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=server__pb2.OkMsg.FromString,
        )
    self.Stop = channel.unary_unary(
        '/Server/Stop',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=server__pb2.OkMsg.FromString,
        )
    self.GetLogs = channel.unary_unary(
        '/Server/GetLogs',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=server__pb2.LogMsg.FromString,
        )
    self.DropLogs = channel.unary_unary(
        '/Server/DropLogs',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=server__pb2.OkMsg.FromString,
        )


class ServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetPlan(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetData(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetState(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetPlan(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SetConfig(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RunNext(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Stop(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetLogs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DropLogs(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfig,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=server__pb2.JsonMsg.SerializeToString,
      ),
      'GetPlan': grpc.unary_stream_rpc_method_handler(
          servicer.GetPlan,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=server__pb2.BlockMsg.SerializeToString,
      ),
      'GetData': grpc.unary_stream_rpc_method_handler(
          servicer.GetData,
          request_deserializer=server__pb2.TimeStampMsg.FromString,
          response_serializer=server__pb2.FrameMsg.SerializeToString,
      ),
      'GetState': grpc.unary_unary_rpc_method_handler(
          servicer.GetState,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=server__pb2.StateMsg.SerializeToString,
      ),
      'SetPlan': grpc.stream_unary_rpc_method_handler(
          servicer.SetPlan,
          request_deserializer=server__pb2.BlockMsg.FromString,
          response_serializer=server__pb2.OkMsg.SerializeToString,
      ),
      'SetConfig': grpc.unary_unary_rpc_method_handler(
          servicer.SetConfig,
          request_deserializer=server__pb2.JsonMsg.FromString,
          response_serializer=server__pb2.OkMsg.SerializeToString,
      ),
      'RunNext': grpc.unary_unary_rpc_method_handler(
          servicer.RunNext,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=server__pb2.OkMsg.SerializeToString,
      ),
      'Stop': grpc.unary_unary_rpc_method_handler(
          servicer.Stop,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=server__pb2.OkMsg.SerializeToString,
      ),
      'GetLogs': grpc.unary_unary_rpc_method_handler(
          servicer.GetLogs,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=server__pb2.LogMsg.SerializeToString,
      ),
      'DropLogs': grpc.unary_unary_rpc_method_handler(
          servicer.DropLogs,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=server__pb2.OkMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Server', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
