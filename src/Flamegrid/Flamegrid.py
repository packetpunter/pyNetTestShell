#!env python

import fire
import json
from datetime import datetime
import os
import csv
import pandas as pd
import numpy as np
from TestUtils import LogEngine 
from Tester import perf, ping, speed, mtr
import TestConfig

_CONFIG = TestConfig.CONFIG
_TARGETS = []

class tester(object):
    
    def _ensure_targets(self):
        global _TARGETS
        if(len(_TARGETS) == 0):
            for host in _CONFIG['default']['targets']:
                print(f"Ensuring default targets. Adding {host}")
                _TARGETS.append(host)
        print(f"targets list is now {len(_TARGETS)}")

    def run(self, itargets, tests):
        global _TARGETS
        _valid_targets = list()
        _valid_tests = list()
        
        if (len(itargets) == 0): self._ensure_targets()
        match itargets: # determine how to proceed for single vs list of hosts
            case str():
                print(f"resetting target list for new single target: {itargets}")
                _TARGETS = list()
                _TARGETS.append(itargets)
            case list():
                _valid_targets = list()
                for t in itargets:

                _TARGETS = itargets
        
        match tests: #determine how to proceed for single test vs list of tests
            case str():
                runner(tests)
            
            case list():
                for i in tests:
                    print(f"found group of tests, test: {i}")
        

        for h in _TARGETS:
            for t in tests:
                print(f"running {t} for {h}")

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


# class route(object):
#     mtr._mtr(self._TARGETS)

# class ping(object):
#     ping.ping_runner(self._TARGETS)

# class perf(object):
#     print("iperf implemented later")

# class speed(object):
#     speed.speed_runner()

class Pipeline(object):
    def __init__(self):
        self.test = tester()
        self.tell = teller()


def run():
    fire.Fire(Pipeline)
