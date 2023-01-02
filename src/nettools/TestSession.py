import pandas as pd
import os
import logging

import dns.resolver

from re import search
from datetime import datetime
from yaml import safe_load
from ipaddress import ip_network

import perf 
import ping
import speed 
import trace 

class TestHistory:
    ''' Top level python object to manage the\n'''\
    '''  history from the various test types,\n'''\
    '''  via read,write to the sqlite database'''
    def _init__(self):
        with open("../Config.yml", "r") as config_file:
            self._basepath = self_load(config_file)['default']['base_path']
    
    def __get_path(self) -> str:
        return self._basepath


class Tester:
    ''' Top level python object to create the \n'''\
    '''  container for the testing data as it \n'''\
    '''  is stored on disk and in memory.\n'''\
    '''  This class is instanciated \n'''\
    '''  once at the beginning and holds all the info.'''
    def __init__(self, tests=[]):
        with open("../Config.yml", "r") as config_file:
            self._CONFIG = safe_load(config_file)

        self._TARGETS = []
        self._base = os.getcwd() + "/" + self._CONFIG['default']['base_path']
        self._now = datetime.now()
        self._fday = self._now.strftime("%Y/%m/%d")
        self._ftime = self._now.strftime("%H:%M")
        self._fpath = self._base + "/output/" + self._fday + "/"

        os.makedirs(self._fpath, exist_ok=True)

        self._LOGFILE = self._fpath + self._CONFIG['tester']['slug'] + \
                "_session_at_" + self._ftime + ".testerLog"
        
        self.logger = logging.getLogger(self._CONFIG['tester']['slug'])
        self.logger.setLevel(logging.INFO)

        self.logfileHandle = logging.FileHandler(self._LOGFILE)
        self.logfileHandle.setLevel(logging.INFO)

        self._formatter = logging.Formatter(
                "%(asctime)s::%(name)s::%(levelname)s: %(message)s", 
                datefmt = "%Y-%m-%d-T-%I:%M:%S %p")
        self.logfileHandle.setFormatter(self._formatter)

        self.logger.addHandler(self.logfileHandle)

        self._runners(tests)

    def _logprint(self, msg):
        ''' print to console and log '''
        print(msg)
        self.logger.info(msg)

    def _runners(self, test) -> None:
        ''' execute the runner for the task '''
        self._ensure_targets()
        for t in test:
            match t:
                case 'speed':
                    speed.speed_runner()
                case 'route'|'routes':
                    trace.trace_runner(self._TARGETS)
                case 'ping'|'pings':
                    ping.ping_runner(self._TARGETS)
                case 'perf'|'iperf':
                    self._logprint("iPerf3 test implemented in future release")
                case default:
                    self._logprint(f"Unable to match test {test}")
                    return 
        self._logprint("Test executed")
                
    def _ensure_targets(self):
        if(len(self._TARGETS) == 0):
            for host in self._CONFIG['default']['targets']:
                self.logger.debug(f"Ensuring default targets. Adding {host}")
                self._TARGETS.append(host)
        else:
            self.logger.debug("validating user specified targets.")
            for host in self._TARGETS:
                host = self._cleantarget(host)
            self._logprint("Valid targets exist.")

    def _cleantarget(self, target) -> str:
        ''' validate targets to add.\n '''\
        ''' this method validates that the target is '''\
        ''' an IP address, and if it isnt, \n'''\
        ''' it tries to convert it to one via dns.\n'''\
        ''' if it cannot convert the target IP, it returns nothing.'''

        _temp_target = ""

        try:
            _temp_target = ip_network(target)
            if(_temp_target.prefixlen == 32):
                return str(_temp_target.network_address)
            else:
                _t = _temp_target.network_address + 1
                self._logprint(f"Target is network. Targeting {_t}")
                return self(_t)
        
        except ValueError as v:
            if("host bits" in repr(v)):
                self.logger.error(f"IP was for a CIDR. Must be single host only! Skipping {target}!")
                return ""
            if("does not appear to be" in repr(v)):
                self._logprint(f"Target {target} is not apparently ip, converting")

                # source oreilly
                # source url https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch08s15.html
                domain_regex = "\A([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\Z"
                match_result = search(domain_regex, target)
                if match_result:
                    real_result = match_result.string
                    self.logger.info("target is valid domain name..")
                    try:
                        resolved_ip = dns.resolver.resolve(real_result, "A")
                        self._logprint(f"validated {target}->ip {resolved_ip}")
                        return resolved_ip
                    except DNSException:
                        self._logprint(f"Unable to resolve {target}. Skipping..")
                        return ""
                else:
                    self._logprint(f"invalid host specified {target}. not adding to target list.")
                    return ""
     
    def _get_targets(self) -> list:
        return self._TARGETS

    def _set_targets(self, targetList):
        self._logprint("Targets cleared and reset")
        for target in targetList:
            target = self._cleantarget(target)

        self._TARGETS = []
        self._TARGETS = targetList.copy()

    def _get_path(self) -> str:
        return self._base

