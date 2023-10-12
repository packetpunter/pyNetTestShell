import os
from datetime import datetime
import TestConfig
from TestUtils.TestObjects import TestType, TestResult
from tabulate import tabulate
from pathlib import Path

class TestHistory:
    ''' Top level python object to manage the\n'''\
    '''  history from the various test types,\n'''\
    '''  via read,write to the '''
    def __init__(self):
        self._basepath = TestConfig.CONFIG['default']['base_path']
        self._now = datetime.now()
        self._fday = self._now.strftime("%Y/%m/%d")
        self._ftime = self._now.strftime("%H:%M")
        self._fpath = Path.home().as_posix() + "/" + self._basepath + "/" + self._fday + "/"
        os.makedirs(self._fpath, exist_ok=True)
        self._logfile = self._fpath + "log.txt"
    
    def __get_path(self) -> str:
        return self._logfile
    
    #TODO: implement storage of results as pandas dataframes
    #def append_raw()
    
    def append(self, result: TestResult, test_type: str) -> None:
        ''' convert log message to db entry '''
        #TODO: convert from print statement in Logging->TestHistory.append() to permament storage for query
        pretty_result = "\n" + tabulate(result, headers='keys', tablefmt='fancy_grid')
        print(f"HISTORY LOGGER::: {TestType(test_type)} Result {pretty_result}")
        with open(self._logfile, "a") as f:
            f.write(f"{self._fday} {self._ftime}|  {TestType(test_type)} Result {pretty_result}\n")

    def query(self, host, query_date, test_type):
        '''retreive log from storage'''

        #TODO: implement database for logging in Logging->TestHistory.query() from permanent storage
        print(f'HISTORY ENTRY:: {host} for date {query_date} with test {TestType(test_type)}')
