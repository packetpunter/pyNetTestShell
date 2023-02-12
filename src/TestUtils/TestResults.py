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
    
    def __init__(self):
        self._type = TestType.NONE
        self._result_frame = pd.DataFrame()
        

    @classmethod
    def from_json(self, result_data: str):
        ...

    @classmethod
    def from_csv(self, result_data: str):
        ...
    
    @classmethod
    def from_dict(self, result_data: dict):
        ...
    
    @classmethod
    def from_list(self, result_data: list):
        ...

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
        return self._ts

    @time_stamp.setter
    def time_stamp(self, time_stamp: datetime):
        self._ts = time_stamp.strftime("%Y/%m/%d-T-%H:%M:%S")

    def construct_frame(self, test_data: str) -> pd.DataFrame:
        match str(type(self._raw)):
            case "<class 'PingResult'>":
                pass
            case "<class 'TraceResult'>":
                pass
        the_frame = pd.DataFrame.from_dict(self._raw)
        return the_frame
    
    
