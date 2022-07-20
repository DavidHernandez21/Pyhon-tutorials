from dataclasses import dataclass
from enum import auto
from enum import Enum


class MessageType(Enum):
    """
    type of message Enum
    """

    SWITCH_ON = auto()
    SWITCH_OFF = auto()
    CHANGE_COLOR = auto()
    PLAY_SONG = auto()
    OPEN = auto()
    CLOSE = auto()
    FLUSH = auto()
    CLEAN = auto()


@dataclass
class Message:
    device_id: str
    msg_type: MessageType
    data: str = ""
    duration: float = 0.5
