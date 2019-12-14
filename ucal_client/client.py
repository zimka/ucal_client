"""Ucal Client."""
import grpc
from google.protobuf import empty_pb2

from ucal_client._internal_grpc import server_pb2
from ucal_client._internal_grpc import server_pb2_grpc
from ucal_client.base import UcalState, UcalConfig, UcalClientException

_SERVER_DEFAULT_HOST = "localhost"
_SERVER_DEFAULT_PORT = "10003"


class UcalClient:
    """Wrap over grpc client."""

    def __init__(
            self,
            host=_SERVER_DEFAULT_HOST,
            port=_SERVER_DEFAULT_PORT
        ):
        """
        :param host: IP addrress where server is running
        :param port: port where server is running
        """
        self.host = host
        self.port = port

    @property
    def stub(self):
        """GRPC server stub."""
        if not hasattr(self, "_stub"):
            channel = grpc.insecure_channel(
                "{}:{}".format(self.host, self.port)
            )
            self._stub = server_pb2_grpc.ServerStub(channel)
        return self._stub

    def get_state(self):
        """Return UcalState of the server."""
        return UcalState(
            self.stub.GetState(empty_pb2.Empty()).name
        )

    def get_config(self):
        """Return UcalConfig from the server."""
        return UcalConfig.from_message(
            self.stub.GetConfig(empty_pb2.Empty()).json
        )

    def set_config(self, config):
        """
        Apply new config to the server. Valid action only at NoPlan state.

        :param config: UcalConfig or Dict with valid UcalConfig key-values
        """
        if isinstance(config, dict):
            config = UcalConfig(**config)
        if not isinstance(config, UcalConfig):
            msg = "set_config accepts dict or UcalConfig, got {}".format(
                type(config)
            )
            raise UcalClientException(msg)
        self.stub.SetConfig(
            server_pb2.JsonMsg(config.to_message())
        )
        return True
