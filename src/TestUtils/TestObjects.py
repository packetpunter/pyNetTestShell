from enum import StrEnum, auto
import pandas as pd
from datetime import datetime
from dataclasses import dataclass
from ipaddress import ip_network
from re import search
import dns.resolver
from dns.exception import DNSException

class TestType(StrEnum):
    PERF = auto()
    ROUTE = auto()
    SPEED = auto()
    PING = auto()
    OPCMD = auto()
    ALL = str(420)
    TRACEROUTE = ROUTE


class TestResult():
    
    def __init__(self, test_type: TestType):
        self._test_type = test_type
        self._src_host = ""
        self._dest_host = ""
        self._result_frame = pd.DataFrame()
        self._base_frame_dict = { #base frame for all tests
            "TS": datetime.now().strftime("%Y/%m/%d-T-%H:%M:%S"),
            "SRC": "none",
            "DST": "none",
            "Route_AvgJitter": -1.0,
            "Route_AvgRtt": -1.0,
            "Route_HighestLossHop": "none",
            "Perf_Down": -1.0,
            "Perf_Up": -1.0,
            "Speed_Down": -1.0,
            "Speed_Up": -1.0,
            "Speed_Latency": -1.0,
            "Speed_URL": "none",
            "Ping_Avg": -1.0,
            "Ping_Max": -1.0,
            "Ping_Min": -1.0,
            "Ping_PctLoss": 0.0
        }
        
        self._base_frame = pd.DataFrame(data=self._base_frame_dict, index=["TS"])
        self._base_speed_frame = self._base_frame.copy()
        del self._base_speed_frame["Route_AvgJitter"]
        del self._base_speed_frame["Route_AvgRtt"]
        del self._base_speed_frame["Route_HighestLossHop"]  
        del self._base_speed_frame["Perf_Down"]
        del self._base_speed_frame["Perf_Up"]
        del self._base_speed_frame["Ping_Avg"]
        del self._base_speed_frame["Ping_Max"]
        del self._base_speed_frame["Ping_Min"]
        del self._base_speed_frame["Ping_PctLoss"]
        
        self._base_ping = self._base_frame.copy()
        del self._base_ping["Route_AvgJitter"]
        del self._base_ping["Route_AvgRtt"]
        del self._base_ping["Route_HighestLossHop"]
        del self._base_ping["Perf_Down"]
        del self._base_ping["Perf_Up"]
        del self._base_ping["Speed_Up"]
        del self._base_ping["Speed_Down"]
        del self._base_ping["Speed_Latency"]    
        del self._base_ping["Speed_URL"]  
        
        self._base_perf = self._base_frame.copy()
        del self._base_perf["Ping_Avg"]
        del self._base_perf["Ping_Max"]
        del self._base_perf["Ping_Min"]
        del self._base_perf["Ping_PctLoss"]
        del self._base_perf["Route_AvgJitter"]
        del self._base_perf["Route_AvgRtt"]
        del self._base_perf["Route_HighestLossHop"]
        del self._base_perf["Speed_Up"]
        del self._base_perf["Speed_Down"]
        del self._base_perf["Speed_Latency"]    
        del self._base_perf["Speed_URL"]  
        
        self._base_route = self._base_frame.copy()
        del self._base_route["Speed_Up"]
        del self._base_route["Speed_Down"]
        del self._base_route["Speed_Latency"]    
        del self._base_route["Speed_URL"]  
        del self._base_route["Ping_Avg"]
        del self._base_route["Ping_Max"]
        del self._base_route["Ping_Min"]
        del self._base_route["Ping_PctLoss"]
        del self._base_route["Perf_Down"]
        del self._base_route["Perf_Up"]
        
    def generate_frame(self) -> pd.DataFrame:
        match(self._test_type):
            case TestType.PING:
                return self._base_ping
            case TestType.PERF:
                return self._base_perf
            case TestType.ROUTE:
                return self._base_route
            case TestType.SPEED:
                return self._base_speed_frame
    
    @property
    def src_host(self):
        return self._src_host
    
    @property
    def test_type(self):
        return self._test_type

    @property
    def dest_host(self):
        return self._dest_host

    @property
    def time_stamp(self):
        return self._base_frame["TS"]



@dataclass
class ValidAddress(str):
    validated_ip = ""

    def __init__(self, input_address="127.0.0.1"):
        if input_address == "127.0.0.1":
            print("setting default IP to localhost")
            self.validated_ip = input_address
        else:
            try:
                # TODO: add ipv6 support
                _temp_target = ip_network(input_address)
                if(_temp_target.prefixlen == 32): 
                    self.validated_ip = str(_temp_target.network_address)
                else:
                    _t = _temp_target.network_address + 1
                    print(f"Target is network address. Targeting first host")
                    self.validated_ip = str(_t)
            except ValueError as v:
                if("host bits" in repr(v)):
                    print(f"Target was for a CIDR. Setting to first host in network.")
                    self.validated_ip = str(ip_network(input_address, strict=False).network_address + 1)

                if("does not appear to be" in repr(v)):
                    # source oreilly
                    # source url https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch08s15.html
                    domain_regex = "\A([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\Z"
                    match_result = search(domain_regex, input_address)
                    if match_result:
                        real_result = match_result.string
                        try:
                            dns_response = dns.resolver.resolve(real_result, "A")
                            # source https://stackoverflow.com/questions/49509431/returning-a-dns-record-in-dnspython
                            resolved_ip = "".join([str(dns_response[0], ), ""])
                            self.validated_ip = resolved_ip
                        except DNSException as e:
                            print(f"{e}")       
            finally:
                if self.validated_ip == "":
                    print(f"Invalid target {input_address}, setting to localhost")
                    self.validated_ip = "127.0.0.1"
                if self.validated_ip == "0.0.0.0":
                    print(f"DNS returned an invalid response for {input_address},\n returning address 0.0.0.0..\nThis is likely a network security block.\nSetting to localhost")
                    self.validated_ip = "127.0.0.1"

    def __repr__(self):
        return self.validated_ip



