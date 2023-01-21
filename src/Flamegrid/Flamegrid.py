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

class tester(object):

    def _ensure_targets(self):
    if(len(self._TARGETS) == 0):
        for host in self._CONFIG['default']['targets']:
            #self.logger.debug(f"Ensuring default targets. Adding {host}")
            self._TARGETS.append(host)
        #else:
            #self.logger.debug("validating user specified targets.")
            #for host in self._TARGETS:
            #    host = self._cleantarget(host)
            #self._logprint("Valid targets exist.")

    def run(self, targets=_ensure_targets(), tests=[]):


class analyzer(object):

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
        self._ensure_targets()
        self.tester = run_test()
        self.describe = describe()


def run():
    self._TARGETS = []
    fire.Fire(Pipeline)
