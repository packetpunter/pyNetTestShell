from dataclasses import dataclass, field
from enum import StrEnum, auto
from datetime import datetime
import TestConfig

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

@dataclass(frozen=True)
class TestResult:
    ''' Top level python object to manage the log formatting'''
    src_host: str
    dest_host: str
    status: str
    test_type: str
    time_stamp: datetime = field(repr=False)
    results: str = field(compare=False, hash=False, repr=False)
    logfile: str = field(compare=False, hash=False)

class TestHistory:
    ''' Top level python object to manage the\n'''\
    '''  history from the various test types,\n'''\
    '''  via read,write to the '''
    def _init__(self):
        self._basepath = TestConfig.CONFIG['default']['base_path']
        self._now = datetime.now()
        self._fday = self._now.strftime("%Y/%m/%d")
        self._ftime = self._now.strftime("%H:%M")
        self._fpath = self._base + self._fday + "/"
        os.makedirs(self._fpath, exist_ok=True)
    
    def __get_path(self) -> str:
        return self._basepath
    
    #TODO: implement storage of results as pandas dataframes
    #def append_raw()
    
    def append(self, host: str, message: str, test_type: str, date: str) -> None:
        ''' convert log message to db entry '''\
        ''' TODO: convert from Print to remove dbl print '''
        print(f"HISTORY LOGGER::: {message} from {host} for {TestType(test_type)}")

    def query(self, host, query_date, test_type):
        print(f'HISTORY ENTRY:: {host} for date {query_date} with test {TestType(test_type)}')
