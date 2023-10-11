#!env python

import fire
import json
from datetime import datetime
import os
import csv
import pandas as pd
import numpy as np
from TestUtils.Logging import TestHistory
import TestConfig
from TestUtils.TestObjects import ValidAddress
from Tester.TestSession import Tester

_CONFIG = TestConfig.CONFIG

class tester(object):
    def __init__(self):
        self._TARGETS = list()

    def defaults(self):
        Tester(test="route", targets=_CONFIG['default']['targets']).run()
        Tester(test="ping", targets=_CONFIG['default']['targets']).run()
        Tester(test="speed", targets=_CONFIG['default']['targets']).run()
         

    def _submit_target(self, target: str):
        self._TARGETS.append(ValidAddress(target))

    def ping(self, target):
        self._submit_target(target)
        Tester("ping", self._TARGETS).run()
        

    def route(self, target):
        self._submit_target(target)
        Tester("route", self._TARGETS).run()

    def speed(self):
        Tester("speed", self._TARGETS).run()

class teller(object):
    
    def history(self, target):

        def ping(self, target):
            print(f"ping history for {target}..")

        def perf(self, target):
            print(f"perf history for {target}..")

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
