from cmd import Cmd
import TestConfig
from Tester.TestSession import Tester
from datetime import datetime
from time import sleep

class shellCmdInteractive(Cmd):
    
    prompt = TestConfig.CONFIG['shell']['slug'] + "> "
    intro = "Welcome to the {} v{} app to test your network!\n\n" \
            "Type ? to list commands.\n For questions, please "\
            "contact the administrator who granted you this access.\n\n".format(
                    TestConfig.CONFIG['shell']['name'],
                    TestConfig.CONFIG['shell']['version'])


    _CONFIG = TestConfig.CONFIG
    _TARGETS= _CONFIG['default']['targets']
    _now = datetime.now()
    _fday = _now.strftime("%Y/%m/%d")
    _ftime = _now.strftime("%H:%M")
    _sleep_interval = _CONFIG['default']['sleep_interval_seconds']

    def _userprint(self, msg):
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
        self._userprint(" *** Goodbye ***!")
        return True


    def do_run(self, verbage):
        ''' execute tests based off verbs'''\
        '''\n e.g run ping \n'''\
        ''' You can run these:\n'''\
        ''' speed, route/routes, ping/pings,\n'''\
        ''' sleep'''
        actions = verbage.split()
        if(len(actions) == 0):
            return
        
        if "all" in actions:
            self._userprint(" 'all' test selected. Running all tests once only")
            Tester("speed").run()
            Tester("route", self._TARGETS).run()
            Tester("ping", self._TARGETS).run()
            Tester("perf", self._TARGETS).run()
            actions = [] #clear actions list so nothing else runs
        
        for action in actions: #loop for multiple run commands, e.g. 'run ping route'
            match action:
                case 'sleep'|'wait':
                    self._sleep()
                case _:
                    Tester(test=action, targets=self._TARGETS).run()

    def do_set(self, user_input):
        ''' set for properties target(s), sleep_interval '''
        actions = user_input.split()
        if(len(actions) == 0):
            return
        action = actions.pop(0)
        match action:
            case 'target'|'targets':
                _targs = []
                for t in actions:
                    _targs.append(t)
                self._TARGETS = _targs.copy()
            case 'sleep'|'sleep_interval':
                try:
                    _nsi = int(actions[0])
                    self._sleep_interval = _nsi
                except ValueError:
                    self._userprint(f"Invalid entry {type(_nsi)}:{_nsi}")
                finally:
                    self._userprint(f"set new sleep interval to {_nsi} seconds")
            case default:
                self._userprint("Attempted to set unknown property {} to val {}".format(action, actions))

    def do_show(self, user_input):
        ''' wrap around get for properties target, targets'''
        self.do_get(user_input)

    def do_get(self, user_input):
        ''' get properties: target, targets, logfile'''
        requested_properties = user_input.split()
        for p in requested_properties:
            match p:
                case 'target'|'targets':
                    self._userprint(self._TARGETS)
                case 'sleep'|'sleep_interval':
                    self._userprint(self._sleep_interval)
                case default:
                    self._userprint("Can't get unknown property {}".format(p))

    def do_open_targets(self, user_input):
        ''' open targets file and load that into memory'''
        with open(user_input, 'r') as f:
            for entry in f:
                if(len(entry.strip()) > 0): self._TARGETS.append(entry)
        self._userprint("Found {} in your targets file!".format(len(self._TARGETS)))

    def do_clear_targets(self, user_input):
        ''' clear target list '''
        self._TARGETS.clear()

    def _sleep(self):
        ''' invoke sleep for default sleep interval in seconds. can be changed with 'set'.'''
        self._userprint(f"sleep invoked for {self._sleep_interval} seconds....\n")
        for i in range(self._sleep_interval):
            sleep(1)


