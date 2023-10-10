from tabulate import tabulate

import TestConfig
from .perf import * 
from .ping import *
from .speed import *
#from .mtr import *

from TestUtils.Logging import TestHistory, TestType
from TestUtils.TestObjects import TestResult
from TestUtils.TestObjects import ValidAddress

class Tester:
    ''' Top level python object to create the \n'''\
    '''  container for the testing data as it \n'''\
    '''  is stored on disk and in memory.\n'''\
    '''  This class is instanciated \n'''\
    '''  once at the beginning and holds all the info.'''
    def __init__(self, test: str, targets: list()):
        self._TEST = test
        self._TARGETS = list()
        if len(targets) > 0:
            self._TARGETS = targets
        self._CONFIG = TestConfig.CONFIG
        self._HISTORY = TestHistory()
    
    def run(self):
        self._ensure_targets()
        self._runner(self._TEST, self._TARGETS)
        
    def _logprint(self, msg):
        ''' print to console and log '''
        print(f"TestSession: {msg}")
        #self._HISTORY.append(msg)

    def _runner(self, test, targets) -> None:
        ''' execute the runner for the task '''
        results = ""
        match test:
            case 'speed':
                self._logprint("Begin speedtest")
                results = speed_runner()
            case 'route'|'routes'|'traceroute'|'mtr'|'trace':
                self._logprint("Begin route testing")
                results = traceroute_runner(targets)
                for r in results:
                    self._logprint(f"TEST {test}:: RESULTS \n{tabulate(r, headers='keys', tablefmt='fancy_grid')}")
                results = []
            case 'ping'|'pings':
                self._logprint("Begin ping tests")
                results = ping_runner(targets)
                for r in results:
                    self._logprint(f"TEST {test}:: RESULTS \n{tabulate(r, headers='keys', tablefmt='fancy_grid')}")
                results = []
            case 'perf'|'iperf':
                self._logprint("Begin iperf test")
                results = "iPerf3 test implemented in future release"
        if results: 
            self._logprint(f"TEST {test}:: RESULTS {results}")
                
    def _ensure_targets(self):
        if(len(self._TARGETS) == 0):
            for host in self._CONFIG['default']['targets']:
                v = ValidAddress(host)
                #self._logprint(f"Ensuring default targets. Adding {v}")
                self._TARGETS.append(v)
        else:
            for host in self._TARGETS:
                host = ValidAddress(host)
                #self._logprint(f"Validated target {host}")
 
    def _get_targets(self) -> list:
        return self._TARGETS

    def _set_targets(self, targetList):
        self._logprint("Targets cleared and reset")
        for target in targetList:
            target = self._cleantarget(target)

        self._TARGETS = []
        self._TARGETS = targetList.copy()


