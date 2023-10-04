import os
from datetime import datetime
import TestConfig
from .TestResults import TestType


class TestHistory:
    ''' Top level python object to manage the\n'''\
    '''  history from the various test types,\n'''\
    '''  via read,write to the '''
    def __init__(self):
        self._basepath = TestConfig.CONFIG['default']['base_path']
        self._now = datetime.now()
        self._fday = self._now.strftime("%Y/%m/%d")
        self._ftime = self._now.strftime("%H:%M")
        self._fpath = self._basepath + "/" + self._fday + "/"
        os.makedirs(self._fpath, exist_ok=True)
    
    def __get_path(self) -> str:
        return self._basepath
    
    #TODO: implement storage of results as pandas dataframes
    #def append_raw()
    
    def append(self, host: str, message: str, test_type: str, date: str) -> None:
        ''' convert log message to db entry '''
        #TODO: convert from print statement in Logging->TestHistory.append() to permament storage for query
        print(f"HISTORY LOGGER::: {message} from {host} for {TestType(test_type)}")

    def query(self, host, query_date, test_type):
        '''retreive log from storage'''

        #TODO: implement database for logging in Logging->TestHistory.query() from permanent storage
        print(f'HISTORY ENTRY:: {host} for date {query_date} with test {TestType(test_type)}')
