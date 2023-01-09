from cmd import Cmd
import config
from tester import TestSession
from yaml import safe_load
import os
from datetime import datetime
import logging

class shellCmdInteractive(Cmd):
    
    prompt = config.CONFIG['shell']['slug'] + "> "
    intro = "Welcome to the {} v{} app to test your network!\n\n" \
            "Type ? to list commands.\n For questions, please "\
            "contact the administrator who granted you this access.\n\n".format(
                    config.CONFIG['shell']['name'],
                    config.CONFIG['shell']['version'])


    _CONFIG = config.CONFIG
    _TARGETS= []
    _TESTER = TestSession.Tester()
    _base = os.getcwd() + "/" + _CONFIG['default']['base_path']
    _now = datetime.now()
    _fday = _now.strftime("%Y/%m/%d")
    _ftime = _now.strftime("%H:%M")
    _fpath = _base + "/output/" + _fday + "/"

    os.makedirs(_fpath, exist_ok=True)

    _LOGFILE = _fpath + _CONFIG['tester']['slug'] + \
                "_session_at_" + _ftime + ".testerLog"

    logger = logging.getLogger(_CONFIG['tester']['slug'])
    logger.setLevel(logging.INFO)

    logfileHandle = logging.FileHandler(_LOGFILE)
    logfileHandle.setLevel(logging.INFO)

    _formatter = logging.Formatter(
            "%(asctime)s::%(name)s::%(levelname)s: %(message)s",
            datefmt = "%Y-%m-%d-T-%I:%M:%S %p")
    logfileHandle.setFormatter(_formatter)

    logger.addHandler(logfileHandle)

    def _logprint(self, msg):
        ''' print to console and log '''
        print(msg)
        self.logger.debug(msg)
    
    def emptyline(self):
        ''' clear last line so it doesnt repeat on enter '''
        ''' credit: https://stackoverflow.com/questions/16479029/python-cmd-execute-last-command-while-prompt-and-empty-line'''
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

    def do_exit(self, user_input):
        ''' exit '''
        self._logprint(" *** Goodbye ***!")
        return True


    def do_run(self, verbage):
        ''' execute tests based off verbs'''\
        '''\n e.g run ping \n'''\
        ''' You can run these:\n'''\
        ''' speed, route/routes, ping/pings,\n'''\
        ''' sleep5m/wait5m, sleep10/wait10,\n'''\
        ''' sleep60/wait60/sleep1m/wait1m\n'''\
        ''' sleep1h/wait1h, sleep30m/wait30m'''

        actions = verbage.split()
        if(len(actions) == 0):
            logger.error("do_run: no actions specified")
            return
        if "all" in actions:
            print(" 'all' test selected. Running all tests once only")
            TestSession.Tester("speed")
            TestSession.Tester("route")
            TestSession.Tester("ping")
            TestSession.Tester("perf")
        
            actions = []

        for action in actions: #loop for multiple run commands, e.g. 'run ping route'
            match action:
                case 'sleep5m'|'sleep_5m'|'wait5m':
                    self._sleep_5m()
                case 'sleep10'|'wait10':
                    self._sleep_10()
                case 'sleep60'|'wait60'|'sleep1m'|'wait1m':
                    self._sleep_60()
                case 'sleep1h'|'wait1h':
                    self._sleep_1h()
                case 'sleep30m'|'wait30m':
                    self._sleep_30m()
                #TODO: FIX - likely takes all args
                case default:
                    TestSession.Tester(action)

    def do_set(self, user_input):
        ''' set for properties target,targets '''
        actions = user_input.split()
        if(len(actions) == 0):
            logprint("do_set: no actions specified")
            return
        action = actions.pop(0)
        match action:
            case 'target'|'targets':
                self._logprint("Targets cleared and reset via set")
                _targs = []
                for t in actions:
                    _targs.append(t)
                self._TARGETS = _targs.copy()
                self.logger.debug("set: new TARGETS len: {}".format(len(self._TARGETS)))

            case default:
                self._logprint("Attempted to set unknown property {} to val {}".format(action, actions))

    def do_show(self, user_input):
        ''' wrap around get for properties target, targets, lofile'''
        self.do_get(user_input)

    def do_get(self, user_input):
        ''' get properties: target, targets, logfile'''
        requested_properties = user_input.split()
        for p in requested_properties:
            match p:
                case 'target'|'targets':
                    print(self._TARGETS)
                case 'logfile':
                    print(self._LOGFILE)
                case default:
                    self._logprint("Can't get unknown property {}".format(p))

    def do_open_targets(self, user_input):
        ''' open targets file and load that into memory'''
        with open(user_input, 'r') as f:
            for entry in f:
                if(len(entry.strip()) > 0): _TARGETS.append(entry)
        self._logprint("Found {} in your targets file!".format(len(_TARGETS)))

    def do_clear_targets(self, user_input):
        ''' clear target list '''
        self._TARGETS.clear()

    def _sleep_10(self):
        ''' invoke 10sec sleep '''
        self._logprint("Sleeping for 10 seconds")
        sleep(10)

    def _sleep_60(self):
        ''' invoke 60 sec sleep '''
        self._logprint("Sleeping for 1 minute")
        sleep(60)

    def _sleep_5m(self):
        ''' invoke 5min sleep '''
        self._logprint("Sleeping for 5 mins")
        sleep(300)

    def _sleep_1h(self):
        ''' invoke 1hr sleep '''
        self._logprint("Sleeping for 1h")
        sleep(3600)

    def _sleep_30m(self):
        ''' invoke 30m sleep '''
        self._logprint("Sleeping for 30m")
        sleep(1800)

