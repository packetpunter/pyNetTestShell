import asyncio
import mtrpacket

#  A simple coroutine which will start an mtrpacket session and
#  ping localhost
async def probe(target):
    async with mtrpacket.MtrPacket() as mtr:
        return await mtr.probe(target)

#  Use asyncio's event loop to start the coroutine and wait for the probe
def main():
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(probe())
    finally:
        loop.close()

    #  Print the probe result
    print(result)

if __name__ == "__main__":
    main()
    