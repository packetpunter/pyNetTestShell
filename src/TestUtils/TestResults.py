from enum import StrEnum, auto
import pandas as pd
from datetime import datetime

class TestType(StrEnum):
    PERF = auto()
    ROUTE = auto()
    SPEED = auto()
    PING = auto()
    OPCMD = auto()
    ALL = str(420)
    NONE = auto()



class TestResult():
    
    def __init__(self, test_type: TestType):
        self._test_type = test_type
        self._src_host = ""
        self._dest_host = ""
        self._result_frame = pd.DataFrame()
        self._base_frame_dict = {
            "TA_TS": datetime.now().strftime("%Y/%m/%d-T-%H:%M:%S"),
            "TA_SRC": "none",
            "TA_DST": "none",
            "TR_Route_HopNum": 0,
            "TR_Route_HopMS": -1.0,
            "TR_Perf_Down": -1.0,
            "TR_Perf_Up": -1.0,
            "TR_Speed_Down": -1.0,
            "TR_Speed_Up": -1.0,
            "TR_Speed_Latency": -1.0,
            "TR_Speed_URL": "none",
            "TR_Ping_Avg": 0.0,
            "TR_Ping_Max": 0.0,
            "TR_Ping_Min": 0.0,
            "TR_Ping_StdDev": 0.0,
            "TR_Ping_PctLoss": 0.0
        }
        self._base_frame = pd.DataFrame(data=self._base_frame_dict, index=["TA_TS"])
        self._frame = self._base_frame.copy()
        self._base_speed = self._base_frame.copy()
        del self._base_speed["TR_Route_HopNum"]
        del self._base_speed["TR_Route_HopMS"]
        del self._base_speed["TR_Perf_Down"]
        del self._base_speed["TR_Perf_Up"]
        del self._base_speed["TR_Ping_Avg"]
        del self._base_speed["TR_Ping_Max"]
        del self._base_speed["TR_Ping_Min"]
        del self._base_speed["TR_Ping_StdDev"]
        del self._base_speed["TR_Ping_PctLoss"]

        self._base_ping = self._base_frame.copy()
        del self._base_ping["TR_Route_HopNum"]
        del self._base_ping["TR_Route_HopMS"]
        del self._base_ping["TR_Perf_Down"]
        del self._base_ping["TR_Perf_Up"]
        del self._base_ping["TR_Speed_Up"]
        del self._base_ping["TR_Speed_Down"]
        del self._base_ping["TR_Speed_Latency"]    
        del self._base_ping["TR_Speed_URL"]  
        
        self._base_perf = self._base_frame.copy()
        del self._base_perf["TR_Ping_Avg"]
        del self._base_perf["TR_Ping_Max"]
        del self._base_perf["TR_Ping_Min"]
        del self._base_perf["TR_Ping_StdDev"]
        del self._base_perf["TR_Ping_PctLoss"]
        del self._base_perf["TR_Route_HopNum"]
        del self._base_perf["TR_Route_HopMS"]
        del self._base_perf["TR_Speed_Up"]
        del self._base_perf["TR_Speed_Down"]
        del self._base_perf["TR_Speed_Latency"]    
        del self._base_perf["TR_Speed_URL"]  
        
        self._base_route = self._base_frame.copy()
        del self._base_route["TR_Speed_Up"]
        del self._base_route["TR_Speed_Down"]
        del self._base_route["TR_Speed_Latency"]    
        del self._base_route["TR_Speed_URL"]  
        del self._base_route["TR_Ping_Avg"]
        del self._base_route["TR_Ping_Max"]
        del self._base_route["TR_Ping_Min"]
        del self._base_route["TR_Ping_StdDev"]
        del self._base_route["TR_Ping_PctLoss"]
        del self._base_route["TR_Perf_Down"]
        del self._base_route["TR_Perf_Up"]

    # @classmethod
    # def from_list(self, result_data: list):
    #     for k,v in result_data:
            
    # @classmethod
    # def from_json(self, result_data: str):
    #     ...

    # @classmethod
    # def from_csv(self, result_data: str):
    #     ...
    
    # @classmethod
    # def from_dict(self, result_data: dict):
    #     ...
    
    @property
    def src_host(self):
        return self._src_host
    
    @src_host.setter
    def src_host(self, src_host: str):
        self._src_host = src_host
    
    @property
    def test_type(self):
        return self._test_type
    
    @test_type.setter
    def test_type(self, test_type: TestType):
        self._test_type = test_type

    @property
    def dest_host(self):
        return self._dest_host

    @dest_host.setter
    def dest_host(self, dest_host: str):
        self._dest_host = dest_host

    @property
    def time_stamp(self):
        return self._base_frame["TA_TS"]

    def __repr__(self):
        return self._frame.to_csv(header=False)
    
    def update(self, data):
        ...
        #TODO: add update frame logic so later classes dont have to use pd.DataFrames
        
    
