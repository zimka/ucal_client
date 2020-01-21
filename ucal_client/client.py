"""Ucal Client implementation."""
from functools import wraps
import grpc
from google.protobuf import empty_pb2
import pandas as pd

from ucal_client._internal_grpc import server_pb2
from ucal_client._internal_grpc import server_pb2_grpc
from ucal_client.base import UcalBlock, UcalState, \
    UcalConfig, UcalClientException, UcalTs

_SERVER_DEFAULT_HOST = "192.168.241.1"
_SERVER_DEFAULT_PORT = "10003"


def grpc_reraise(method):
    """Wrap grpc error into UcalClientException."""
    @wraps(method)
    def reraised_method(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except grpc.RpcError as exc:
            exc_msg = None
            if exc.code() in (
                grpc.StatusCode.UNAVAILABLE,
                grpc.StatusCode.UNKNOWN
            ):
                exc_msg = "Failed to establish connection: {}".format(exc.details())
            elif exc.code() == grpc.StatusCode.INVALID_ARGUMENT:
                exc_msg = "Got invalid input: {}".format(exc.details())
            elif exc.code() == grpc.StatusCode.FAILED_PRECONDITION:
                exc_msg = "Action can't be performed: {}".format(exc.details())
            if exc_msg:
                # No grpc traceback
                raise UcalClientException(exc_msg) from None
            else:
                # Show grpc traceback
                exc_msg = "Server bug, please report: {}".format(exc.details())
                raise UcalClientException(exc_msg)
    return reraised_method


class UcalClient:
    """
    The main object that can be used to manage Ucal Server.
    Client (and Server) supports next actions:
    - get_state to get current state of server, see UcalState;
    - set/get_config to save global settings, see UcalConfig;
    - set/get_plan to set execution program, see UcalBlock;
    - get_data to download from server data as a pandas.DataFrame;
    - run_next/stop to start and stop program execution.
    """
    def __init__(
        self,
        host=_SERVER_DEFAULT_HOST,
        port=_SERVER_DEFAULT_PORT
    ):
        """
        Set host to 'localhost' when server is run locally.
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

    @grpc_reraise
    def get_state(self):
        """
        Return UcalState of the server.
        Possible results: NoPlan, HavePlan, Executing, Error.
        State defines, which actions can or can not be executed by server now.
        """
        return UcalState(
            self.stub.GetState(empty_pb2.Empty()).name
        )

    @grpc_reraise
    def get_config(self):
        """
        Return current server configuration as a UcalConfig.
        Valid action at any state.
        """
        return UcalConfig.from_message(
            self.stub.GetConfig(empty_pb2.Empty()).json
        )

    @grpc_reraise
    def set_config(self, config):
        """
        Apply new config(UcalConfig) to the server.
        Valid action at NoPlan state only.

        :param config: UcalConfig, Str, None or Dict with
            valid UcalConfig key-values
        """
        if isinstance(config, dict):
            config = UcalConfig(**config)
        if isinstance(config, UcalConfig):
            self.stub.SetConfig(
                server_pb2.JsonMsg(json=config.to_message())
            )
            return
        if config is None:
            config = "{}"
        if isinstance(config, str):
            self.stub.SetConfig(
                server_pb2.JsonMsg(json=config)
            )
            return
        msg = "set_config accepts dict, UcalConfig or str, got {}".format(
            type(config)
        )
        raise UcalClientException(msg)

    @grpc_reraise
    def get_plan(self):
        """
        Return plan (List[UcalBlock]) that server is executing or
        going to execute.
        Valid action at NoPlan, HavePlan and Executing states.
        """
        grpc_blocks = list(
            b for b in self.stub.GetPlan(empty_pb2.Empty())
        )
        return list(
            UcalBlock(
                read_step_tu=b.read_step_tu,
                write_step_tu=b.write_step_tu,
                block_len_tu=b.block_len_tu,
                voltage_0=b.voltage_0,
                voltage_1=b.voltage_1
            ) for b in grpc_blocks
        )

    @grpc_reraise
    def set_plan(self, plan):
        """
        Set List[UcalBlock] as a new plan for server.
        Set empty list([]) to move to NoPlan state.
        Valid action at NoPlan and HavePlan states.
        """
        if not (
            isinstance(plan, list) and
            all(isinstance(b, UcalBlock) for b in plan)
        ):
            msg = "Plan must have type List[UcalBlock]"
            raise UcalClientException(msg)
        self.stub.SetPlan(
            (server_pb2.BlockMsg(
                read_step_tu=b.read_step_tu,
                write_step_tu=b.write_step_tu,
                block_len_tu=b.block_len_tu,
                voltage_0=b.voltage_0,
                voltage_1=b.voltage_1
            ) for b in plan)
        )

    @grpc_reraise
    def get_data(self, start_ts=None, merge=True):
        """
        Return List[pd.DataFrame] from Server.
        If merge=True, DataFrames are concatenated.
        DataFrames contain info about voltage and time moments from
        the execution start.

        :param start_ts: UcalTs, starting point for returned data.
        :param merge: bool, whether to concat frames into single df.
        """

        if start_ts is None:
            start_ts = UcalTs(0, 0)
        assert isinstance(start_ts, UcalTs)

        def parse_frame_msg(msg):
            """Turn server_pb2.FrameMsg into pd.DataFrame."""
            df = pd.DataFrame()
            for c in msg.data.keys():
                df[c] = msg.data[c].data
            df['step'] = msg.ts.step
            # TimeStamp in frame is related to the last point
            df['count'] = list(
                x for x in range(msg.ts.count, msg.ts.count + len(df))
            )
            return df
        raw_data = (self.stub.GetData(
            server_pb2.TimeStampMsg(step=start_ts.step, count=start_ts.count))
        )

        separate_dfs = list(parse_frame_msg(r) for r in raw_data)
        if merge:
            # TODO: check not-empty
            df = pd.concat(separate_dfs).reset_index(drop=True)
            df['Time'] = df['step'].cumsum()
            df = df.drop(columns=['count', 'step'])
            return df.set_index('Time')
        else:
            return separate_dfs

    @grpc_reraise
    def run_next(self):
        """
        Start next block execution.
        Valid action at HavePlan, Executing states.
        If server is at HavePlan state, execution is started.
        If server is at Executing state, current UcalBlock execution is
        stopped and next UcalBlock in plan is started.
        If there is no more UcalBlock in plan, execution is finished and
        HavePlan state is set.
        """
        return self.stub.RunNext(empty_pb2.Empty())

    @grpc_reraise
    def stop(self):
        """
        Stop blocks execution. All measured data is available.
        Valid action at Executing state.
        """
        return self.stub.Stop(empty_pb2.Empty())

    @grpc_reraise
    def get_logs(self):
        """Return current server logs."""
        return str(self.stub.GetLogs(empty_pb2.Empty()).row)

    @grpc_reraise
    def drop_logs(self):
        """Drop current server logs."""
        self.stub.DropLogs(empty_pb2.Empty())
