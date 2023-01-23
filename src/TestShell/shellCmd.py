from cmd import Cmd
import TestConfig
from Tester.TestSession import Tester
import os
from datetime import datetime
import logging
from time import sleep
from tqdm import tqdm

class shellCmdInteractive(Cmd):
    
    prompt = TestConfig.CONFIG['shell']['slug'] + "> "
    intro = "Welcome to the {} v{} app to test your network!\n\n" \
            "Type ? to list commands.\n For questions, please "\
            "contact the administrator who granted you this access.\n\n".format(
                    TestConfig.CONFIG['shell']['name'],
                    TestConfig.CONFIG['shell']['version'])


    _CONFIG = TestConfig.CONFIG
    _TARGETS= []
    _now = datetime.now()
    _fday = _now.strftime("%Y/%m/%d")
    _ftime = _now.strftime("%H:%M")
    _sleep_interval = _CONFIG['default']['sleep_interval_seconds']

    def _logprint(self, msg):
        ''' print to console and log '''
        print(msg)
        
    
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
            self._logprint("do_run: no actions specified")
            return
        if "all" in actions:
            print(" 'all' test selected. Running all tests once only")
            with tqdm(total=100) as pbar:
                Tester("speed").run()
                pbar.update(25)
                Tester("route", self._TARGETS).run()
                pbar.update(25)
                Tester("ping", self._TARGETS).run()
                pbar.update(25)
                Tester("perf", self._TARGETS).run()
                pbar.update(25)
            pbar.close()
        
            actions = []
        with tqdm(total=100) as pbar:
            if len(actions) >= 1:
                _pbar_upp = round(float(1/len(actions)*100))
            else:
                _pbar_upp = 1
            for action in actions: #loop for multiple run commands, e.g. 'run ping route'
                match action:
                    case 'sleep'|'wait':
                        self._sleep()
                        pbar.update(_pbar_upp)
                    case _:
                        pbar.update(_pbar_upp)
                        Tester(test=action, targets=self._TARGETS).run()
        pbar.close()

    def do_set(self, user_input):
        ''' set for properties target,targets '''
        actions = user_input.split()
        if(len(actions) == 0):
            self._logprint("do_set: no actions specified")
            return
        action = actions.pop(0)
        match action:
            case 'target'|'targets':
                self._logprint("Targets cleared and reset via set")
                _targs = []
                for t in actions:
                    _targs.append(t)
                self._TARGETS = _targs.copy()
                self._logprint(f"set new targets list that is {self._TARGETS} entries long")
            case 'sleep'|'sleep_interval':
                try:
                    _nsi = int(actions[0])
                    self._sleep_interval = _nsi
                except ValueError:
                    self._logprint(f"Invalid entry {type(_nsi)}:{_nsi}")
                finally:
                    self._logprint(f"set new sleep interval to {_nsi}")
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
                case 'sleep'|'sleep_interval':
                    print(self._sleep_interval)
                case default:
                    self._logprint("Can't get unknown property {}".format(p))

    def do_open_targets(self, user_input):
        ''' open targets file and load that into memory'''
        with open(user_input, 'r') as f:
            for entry in f:
                if(len(entry.strip()) > 0): self._TARGETS.append(entry)
        self._logprint("Found {} in your targets file!".format(len(self._TARGETS)))

    def do_clear_targets(self, user_input):
        ''' clear target list '''
        self._TARGETS.clear()

    def _sleep(self):
        ''' invoke sleep for default sleep interval in seconds. can be changed with 'set'.'''
        self._logprint(f"sleep invoked for {self._sleep_interval} seconds....\n")
        for i in range(self._sleep_interval):
            sleep(1)


