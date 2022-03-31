import asyncio
from typing import Any, Awaitable

from iot.devices import HueLightDevice, SmartSpeakerDevice, SmartToiletDevice
from iot.message import Message, MessageType
from iot.service import IOTService


async def run_sequence(*functions: Awaitable[Any]) -> None:
    for function in functions:
        await function


async def run_parallel(*functions: Awaitable[Any]) -> None:
    await asyncio.gather(*functions)


async def main() -> None:
    # create a IOT service
    service = IOTService()

    # create and register a few devices
    hue_light = HueLightDevice()
    speaker = SmartSpeakerDevice()
    toilet = SmartToiletDevice()

    hue_light_id, speaker_id, toilet_id = await asyncio.gather(
        service.register_device(hue_light),
        service.register_device(speaker),
        service.register_device(toilet),
    )

    # create a few programs
    wake_up_program_parallel = (
        Message(hue_light_id, MessageType.SWITCH_ON),
    )

    wake_up_program_sequencial = (
        Message(speaker_id, MessageType.SWITCH_ON),
        Message(speaker_id, MessageType.PLAY_SONG, "Miles Davis - Kind of Blue"),
    )

    sleep_program_parallel = (
        Message(hue_light_id, MessageType.SWITCH_OFF),
        Message(speaker_id, MessageType.SWITCH_OFF),
    )

    sleep_program_sequencial = (
        Message(toilet_id, MessageType.FLUSH, duration=5),
        Message(toilet_id, MessageType.CLEAN),
    )

    # run the programs
    # await service.run_program(wake_up_program)
    # await run_parallel(
    #     service.send_msg(Message(hue_light_id, MessageType.SWITCH_OFF)),
    #     service.send_msg(Message(speaker_id, MessageType.SWITCH_OFF)),
    #     run_sequence(
    #         service.send_msg(Message(toilet_id, MessageType.FLUSH)),
    #         service.send_msg(Message(toilet_id, MessageType.CLEAN)),
    #     ),
    # )

    functions_parallel_wakeup = (service.send_msg(msg) for msg in wake_up_program_parallel)
    functions_sequencial_wakeup = (service.send_msg(msg) for msg in wake_up_program_sequencial)
    await service.run_program_parseq(functions_parallel=functions_parallel_wakeup,
                                     functions_sequence=functions_sequencial_wakeup)

    functions_parallel_sleep = (service.send_msg(msg) for msg in sleep_program_parallel)
    functions_sequencial_sleep = (service.send_msg(msg) for msg in sleep_program_sequencial)
    await service.run_program_parseq(functions_parallel=functions_parallel_sleep,
                                     functions_sequence=functions_sequencial_sleep)

if __name__ == "__main__":
    asyncio.run(main())