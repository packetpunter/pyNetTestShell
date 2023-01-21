from dataclasses import dataclass, field
from enum import StrEnum, auto
from abc import ABC, abstractmethod
import pandas as pd
from datetime import datetime

'''
>>> a = TestResult(host="tits", status="failed", test_type="420", time_stamp = datetime.now() )
>>> a
TestResult(host='tits', status='failed', test_type='420')
>>> a.time_stamp
datetime.datetime(2023, 1, 21, 0, 16, 28, 913384)
>>> TestType(a.test_type)
<TestType.ALL: '420'>
>>> TestType(a.test_type)
<TestType.ALL: '420'>
'''
class TestType(StrEnum):
    PERF = auto()
    ROUTE = auto()
    SPEED = auto()
    PING = auto()
    OPCMD = auto()
    ALL = str(420)

# @dataclass(frozen=True)
# class TestResult:
#     ''' Top level python object to manage the log formatting'''
#     src_host: str
#     dest_host: str
#     status: str
#     test_type: str
#     time_stamp: datetime = field(repr=False)
#     results: str = field(compare=False, hash=False, repr=False)
#     logfile: str = field(compare=False, hash=False)

class TestResultInterface(ABC):
    @abstractmethod
    @classmethod
    def from_json(self, result_data: str):
        ...

    @abstractmethod
    @classmethod
    def from_csv(self, result_data: str):
        ...
    
    @abstractmethod
    @classmethod
    def from_dict(self, result_data: dict):
        ...
    
    @abstractmethod
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

    @abstractmethod
    def construct_frame(self, test_data: str) -> pd.DataFrame:
        match str(type(self._raw)):
            case "<class 'PingResult'>":
                pass
            case "<class 'TraceResult'>":
                pass
        the_frame = pd.DataFrame.from_dict(self._raw)
        return the_frame
    
class PingResult(TestResultInterface):
    ''' implementor'''

    def construct_frame(self, test_data: str) -> pd.DataFrame:
        return super().construct_frame(test_data)
    
