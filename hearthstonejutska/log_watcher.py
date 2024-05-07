import asyncio
from io import TextIOWrapper


async def monitor(logfile: TextIOWrapper):
    logfile.seek(0, 2)
    while True:
        await signal
        line = logfile.readline()



async def async_monitor(logfile: TextIOWrapper):
    """
    Async generator function that yields lines from logfile as they are written.

    :param logfile:
    :return:
    """
    logfile.seek(0, 2)
    while True:
        line = logfile.readline()
        if not line:
            await asyncio.sleep(0.1)
            continue
        yield line
