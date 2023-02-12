import asyncio
import sys
import mtrpacket
from TestUtils.Testing import ValidAddress, TestType, AsyncBackgroundTask, asyncRunner

#source https://raw.githubusercontent.com/matt-kimball/mtr-packet-python/master/examples/ping.py
#
#  We send the probe in a coroutine since mtrpacket operates
#  asynchronously.  In a more complicated program, this
#  allows other asynchronous operations to occur concurrently
#  with the probe.
#
#@AsyncBackgroundTask
async def asping(host: ValidAddress):
    res_dict = {}
    total_ms = 0

    # async with mtrpacket.MtrPacket() as mtr:
    #     for i in range(repeat_count):
    #         result = await mtr.probe(host, size=900)

    #         # If the ping got a reply, report the IP address and time
    #         if result.success:
    #             # print('reply from {} in {} ms'.format(
    #             #     result.responder, result.time_ms))
    #             total_ms += result.time_ms
    #         else:
    #             print('no reply ({})'.format(result.result))
    mtr = mtrpacket.MtrPacket()
    result = await mtr.probe(host, size=900) 
    res_dict = {'hostname': host, 'avg_ms': round(total_ms/10, 3)}
    print(res_dict)
    #return PingResult.construct_timeframe_from_csv(csv.)

def run(target: str):
    #loop = asyncio.get_event_loop()
    #try:
        #probe_coroutine = asping(target, 10)
        #try:
            #loop.run_until_complete(probe_coroutine)
        #except mtrpacket.HostResolveError:
            #print("Can't resolve host '{}'".format(target))
    #finally:
        #loop.close()
 
    #with asyncio.Runner() as runner:
    result = asyncio.run(asping(target))
    return result
    
        