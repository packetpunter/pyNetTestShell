#!env python

import fire
import json
from datetime import datetime
import os
import csv
import pandas as pd
import numpy as np
from TestUtils import LogEngine 
import TestConfig
from TestUtils.TestTargets import ValidAddress
from Tester.TestSession import Tester

_CONFIG = TestConfig.CONFIG

class tester(object):
    def __init__(self):
        self._TARGETS = list()
        self._TESTS = list()

    def _ensure_targets(self):
        if(len(self._TARGETS) == 0):
            for host in _CONFIG['default']['targets']:
                self._TARGETS.append(ValidAddress(host))
        print(f"targets list is now {len(self._TARGETS)}")

    def run(self, itargets: tuple(), tests: tuple()):

        if (len(itargets) == 0): 
            self._ensure_targets()
        
        if "," in itargets:
            for x in itargets.split(","):
                self._TARGETS.append(ValidAddress(x))
        else:
            self._TARGETS = itargets
        
        if "," in tests:
            for x in tests.split(","):
                self._TESTS.append(x)
        else:
            self._TESTS = tests
        
        for t in self._TESTS:
            print(f"Spawning Tester with Test {t} against host set {self._TARGETS}")
            _tester = Tester(test=t, targets=self._TARGETS)
            _tester.run()

class teller(object):
    
    def history(self, target):

        def ping(self, target):
            print(f"ping history for {target}..")

        def perf(self, target):
            print("perf history for {target}..")

        def route(self, target):
            print(f"route history for {target}")

        def speed(self):
            print("my speed history..")

class Pipeline(object):
    def __init__(self):
        self.test = tester()
        self.tell = teller()

def run():
    fire.Fire(Pipeline)
