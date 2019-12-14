"""IO parts of ucal_client."""
from enum import Enum
from collections import namedtuple
import json

import numpy as np


class UcalClientException(ValueError):
    """Error caused by invalid client usage."""


class UcalBlock:
    """Description of device read/write configuration."""

    __slots__ = [
        "read_step_tu",
        "write_step_tu",
        "block_len_tu",
        "voltage_0",
        "voltage_1"
    ]
    _VOLTAGE_MAX = 10000
    _VOLTAGE_MIN = -10000

    def __init__(self, read_step_tu, write_step_tu, block_len_tu,
                 voltage_0, voltage_1):
        """
        :param read_step_tu: int, time between adc signal measurements
            in time units.
        :param write_step_tu: int, time between dac control update in
            time units.
        :param block_len_tu: int, total duration of block in time
            units. Zero means infinite block.
        :param voltage_0: None or Iterable[int], millivolts array pattern that
            would be repeated at channel 0.
        :param voltage_1: None or Iterable[int], millivolts array pattern that
            would be repeated at channel 1.
        """
        self.read_step_tu = read_step_tu
        self.write_step_tu = write_step_tu
        self.block_len_tu = block_len_tu
        self.voltage_0 = voltage_0
        self.voltage_1 = voltage_1
        if self.voltage_0 is not None:
            self.voltage_0 = np.array(voltage_0).astype(np.int32)
        if self.voltage_1 is not None:
            self.voltage_1 = np.array(voltage_1).astype(np.int32)
        self._validate()

    def _validate(self):
        """Validate UcalBlock attributes."""
        try:
            for attr in ["read_step_tu", "write_step_tu", "block_len_tu"]:
                val = getattr(self, attr)
                assert isinstance(val, int), "'{}' must be int".format(attr)
                assert val >= 0, "'{}' must be non-negative".format(attr)
            for attr in ["voltage_0", "voltage_1"]:
                val = getattr(self, attr)
                if val is not None:
                    assert np.max(val) <= self._VOLTAGE_MAX
                    assert np.min(val) >= self._VOLTAGE_MIN
            if (self.voltage_0 is not None) and (self.voltage_1 is not None):
                msg = "voltage_0 and voltage_1 must have same len if given"
                assert len(self.voltage_0) == len(self.voltage_1), msg
            if (self.voltage_0 is not None) or (self.voltage_0 is not None):
                msg = "write_step_tu must be non-zero when voltage is given"
                assert self.write_step_tu > 0
        except AssertionError as exc:
            msg = "Invalid block configuration: {}".format(str(exc))
            raise UcalClientException(msg)


class UcalState(Enum):
    """
    State of the Server.

    :param EXECUTING: Server is executing Block.
    :param HAVE_PLAN: Server is ready to execute Blocks.
    :param NO_PLAN: Server is waiting for Blocks from client.
    :param ERROR: Server is in emergency state which needs manual fix.
    """

    EXECUTING = 'Executing'
    HAS_PLAN = 'HasPlan'
    NO_PLAN = 'NoPlan'
    ERROR = 'Error'


UcalConfig_ = namedtuple(
    "UcalConfig_", [
        "board_id",
        "time_unit_size",
        "storage_frame_size"
    ]
)


class UcalConfig(UcalConfig_):
    """
    Configuration of the Server.

    :param board_id: str, name that used to init daqboard.
    :param time_unit_size: float, multiplier for millisecond, e.g. 10 or 0.01
    :param storage_frame_size: int, enforce size of frame in server;
        zero means size may vary.
    """

    def to_message(self):
        """Serialize data in json string for server."""
        assert self.time_unit_size >= 0
        try:
            data = {
                "BoardId": str(self.board_id),
                "TimeUnitSize": float(self.time_unit_size),
                "StorageFrameSize": int(self.storage_frame_size)
            }
        except ValueError as exc:
            raise UcalClientException(str(exc))
        return json.dumps(data)

    @classmethod
    def from_message(cls, message):
        """Deserialize data from json string from server."""
        data = json.loads(message)
        board_id = str(data["BoardId"])
        time_unit_size = float(data["TimeUnitSize"])
        storage_frame_size = int(data["StorageFrameSize"])
        return cls(board_id, time_unit_size, storage_frame_size)
