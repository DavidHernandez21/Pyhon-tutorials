from abc import ABC
from abc import abstractmethod
from dataclasses import dataclass
from dataclasses import field

from stream import data


@dataclass
class StreamingService(ABC):
    devices: list[data.Buffer] = field(default_factory=list)

    def add_device(self, device: data.Buffer) -> None:
        self.devices.append(device)

    def retrieve_buffer_data(self) -> list[data.BufferData]:
        return [device() for device in self.devices]

    @abstractmethod
    def start_stream(self) -> str:
        pass

    @abstractmethod
    def fill_buffer(self, stream_reference: str) -> None:
        pass

    @abstractmethod
    def stop_stream(self, stream_reference: str) -> None:
        pass
