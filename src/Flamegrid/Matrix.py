#!env python

import fire
import json
from datetime import datetime
import os
import csv
import pandas as pd
import numpy as np
from AthenianTalismans import LogEngine, TestType
from Tester import perf, ping, speed, mtr

class route(object):
    mtr.run()
class ping(object):
    ping.run()

class perf(object):
    perf.run()

class Pipeline(object):
    def __init__(self):
        self._ensure_targets()
        self.ResultStore = ResultStore()

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
def run():
    self._TARGETS = []
    fire.Fire(Pipeline)
