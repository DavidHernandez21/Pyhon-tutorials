import asyncio
import random
import string
from typing import Any, Awaitable, Protocol, Iterable

from iot.message import Message, MessageType


def generate_id(length: int = 8):
    return "".join(random.choices(string.ascii_uppercase, k=length))


class Device(Protocol):
    async def connect(self) -> None:
        ...

    async def disconnect(self) -> None:
        ...

    async def send_message(self, message_type: MessageType, data: str = "", duration: float = .5) -> None:
        ...


class IOTService:
    def __init__(self):
        self.devices: dict[str, Device] = {}

    async def register_device(self, device: Device) -> str:
        await device.connect()
        device_id = generate_id()
        self.devices[device_id] = device
        return device_id

    async def unregister_device(self, device_id: str) -> None:
        await self.devices[device_id].disconnect()
        del self.devices[device_id]

    def get_device(self, device_id: str) -> Device:
        return self.devices[device_id]

    async def run_program(self, program: list[Message]) -> None:
        print("=====RUNNING PROGRAM======")
        await asyncio.gather(*[self.send_msg(msg) for msg in program])
        print("=====END OF PROGRAM======")

    async def run_program_parallel(self, *functions: Awaitable[Any]) -> None:
        print("=====RUNNING PROGRAM IN PARALLEL======")
        await asyncio.gather(*functions)
        print("=====END OF PROGRAM IN PARALLEL======")

    async def run_program_sequence(self, *functions: Awaitable[Any]) -> None:

        print("=====RUNNING PROGRAM IN SEQUENCE======")
        for function in functions:

            await function

        print("=====END OF PROGRAM IN SEQUENCE======")

    async def run_program_parseq(self, functions_parallel: Iterable[Awaitable[Any]],
                                 functions_sequence: Iterable[Awaitable[Any]]) -> None:
        print("=====RUNNING PROGRAM======")
        await self.run_program_parallel(*functions_parallel, self.run_program_sequence(*functions_sequence))
        print("=====END OF PROGRAM======")

    async def send_msg(self, msg: Message) -> None:
        await self.devices[msg.device_id].send_message(msg.msg_type, msg.data, duration=msg.duration)