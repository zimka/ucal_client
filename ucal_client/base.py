"""Basic parts of ucal_client."""


class Block:
    """Description of device read/write configuration."""

    __slots__ = [
        "read_step_tu",
        "write_step_tu",
        "block_len_tu",
        "voltage_0",
        "voltage_1"
    ]

    def __init__(self, **kwargs):
        for (k, v) in kwargs.items():
            setattr(self, k, v)

    def to_dict(self):
        """Return dict representation of block."""
        return dict((x, getattr(self, x)) for x in self.__slots__)
