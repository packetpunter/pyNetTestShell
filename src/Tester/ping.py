from pandas import DataFrame
from TestUtils.TestObjects import TestResult
from icmplib import ping, traceroute, multiping, resolve
from termcolor import colored, cprint

def ping_runner(targetList) -> list:
    _TARGETS = targetList
    results = _pinger(_TARGETS)
    return results

def traceroute_runner(targetList):
    _TARGETS = targetList
    results = _tracerouter(_TARGETS)
    return results

def _pinger(targetList, logging_enabled=True) -> list:
    result_list = []
    for host in targetList:
        ping_result = ping(host, count=10, interval=1, privileged=False)
        result_list.append(tuple((host, ping_result)))
    results = parse_ping(result_list)
    return results

def _tracerouter(targetList, logging_enabled=True):
    results_list = []
    for host in targetList:
        hop_list = traceroute(host)
        parsed_results = _zparse_trace(host, hop_list)
        results_list.append(parsed_results)
    return results_list

def parse_ping(ping_result_list) -> list:
    result_list = []
    ping_template = TestResult("ping")
    for result in ping_result_list:
        (target, ping_result) = result
        new_result = ping_template.generate_frame()
        new_result["SRC"] = colored("self", "white", "on_blue")
        new_result["DST"] = target
        new_result["Ping_Min"] = ping_result.min_rtt
        new_result["Ping_Max"] = ping_result.max_rtt
        new_result["Ping_Avg"] = ping_result.avg_rtt
        if(ping_result.packet_loss > 0.0):
            new_result["Ping_PctLoss"] = colored(ping_result.packet_loss, "black", "on_red")
        new_result["Ping_PctLoss"] = ping_result.packet_loss
        result_list.append(new_result)
    return result_list

def _zparse_trace(host, hop_list) -> DataFrame:
    trace_template = TestResult("route")
    total_jitter = 0.0
    highest_rtt_hop = dict(address="", rtt=0.0)
    first_hop = hop_list[0].address
    for theHop in hop_list: 
        # print("***Hop: {}".format(theHop))
        if theHop.avg_rtt > highest_rtt_hop["rtt"]:
            highest_rtt_hop = dict(address=theHop.address, rtt=theHop.avg_rtt)
        total_jitter =+ theHop.jitter
        total_rtt =+ theHop.avg_rtt
    
    trace_frame = trace_template.generate_frame()
    src_str = colored(f"self via {first_hop}", "white", "on_blue")
    trace_frame["SRC"] = src_str
    trace_frame["DST"] = host
    trace_frame["Route_AvgJitter"] = total_jitter / len(hop_list)
    trace_frame["Route_AvgRtt"] = total_rtt / len(hop_list)
    highest_hop_str = colored(str(highest_rtt_hop["address"] + " responded in " + str(highest_rtt_hop["rtt"]) + "ms"), "red", "on_black")
    trace_frame["Route_HighestLossHop"] = highest_hop_str
    return trace_frame