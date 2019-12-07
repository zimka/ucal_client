"""Ucal Client."""
import grpc
from ucal_client._internal_grpc import server_pb2
from ucal_client._internal_grpc import server_pb2_grpc
from google.protobuf import empty_pb2


class UcalClient:
    """Wrap over grpc client."""
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def _init_grpc(self):
        channel = grpc.insecure_channel("{}:{}".format(self.host, self.port))
        self._stub = server_pb2_grpc.ServerStub(channel)

    @property
    def stub(self):
        if not hasattr(self, "_stub"):
            self._init_grpc()
        return self._stub

    def get_state(self):
        return self.stub.GetState(empty_pb2.Empty())

    def get_config(self):
        return self.stub.GetConfig(empty_pb2.Empty())
