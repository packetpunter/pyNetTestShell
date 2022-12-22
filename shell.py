from cmd import Cmd
import Config
import pandas as pd
import os
from datetime import datetime
import logging
import subprocess
import speedtest
from io import StringIO
from time import sleep

class nms_interactive(Cmd):
    prompt = Config._PROGRAM_SLUG + "> "
    intro = "Welcome to the {} v{} app to test your network!\n\n" \
            "Type ? to list commands.\n For questions, please "\
            "contact the administrator who granted you this access.\n\n".format(
                    Config._PROGRAM_NAME,
                    Config._VERSION)
    _TARGETS = []
    _cwd = os.getcwd()
    _now = datetime.now()
    _fday = _now.strftime("%Y/%m/%d")
    _ftime = _now.strftime("%H:%M")
    _path = _cwd + "/output/" + _fday + "/" 
    
    os.makedirs(_path, exist_ok=True)
    
    _LOGFILE = _path + Config._PROGRAM_SLUG + "_sessionat_" + _ftime + ".nmsLog"
    
    logger = logging.getLogger(Config._PROGRAM_SLUG)
    logger.setLevel(logging.DEBUG)

    logfileHandle = logging.FileHandler(_LOGFILE)
    logfileHandle.setLevel(logging.INFO)
    
    formatter = logging.Formatter("%(asctime)s::%(name)s::%(levelname)s: %(message)s", datefmt="%Y-%m-%d-T-%I:%M:%S %p")
    logfileHandle.setFormatter(formatter)

    logger.addHandler(logfileHandle)

    def emptyline(self):
        ''' clear last line so it doesnt repeat on enter '''
        ''' credit: https://stackoverflow.com/questions/16479029/python-cmd-execute-last-command-while-prompt-and-empty-line'''
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd("\n")

    def do_exit(self, user_input):
        ''' exit '''
        print("Exiting per user..")
        return True

    def _sleep_10(self):
        ''' invoke 10sec sleep '''
        msg = "Sleeping for 10 seconds"
        self.logger.info(msg)
        print(msg)
        sleep(10)

    def _sleep_60(self):
        ''' invoke 60 sec sleep '''
        msg = "Sleeping for 1 minute"
        self.logger.info(msg)
        print(msg)
        sleep(60)

    def _sleep_5m(self):
        ''' invoke 5min sleep '''
        msg = "Sleeping for 5 mins"
        self.logger.info(msg)
        print(msg)
        sleep(300)
        
    def do_run(self, verbage):
        ''' execute tests based off verbs'''\
        '''\n e.g run ping \n'''\
        ''' You can run these:\n'''\
        ''' speed, route/routes, ping/pings,\n'''\
        ''' sleep5m/wait5m, sleep10/wait10,\n'''\
        ''' sleep60/wait60/sleep1m/wait1m\n'''

        actions = verbage.split()
        if(len(actions) == 0):
            self.logger.error("do_run: no actions specified")
            return
        if "all" in actions:
            print(" 'all' test selected. Running all tests once only")
            self._speedtest()
            self._pingonce()
            self._mtr()
            actions = []
        for action in actions: #loop for multiple run commands, e.g. 'run ping route'
            match action:
                case 'speed':
                    self._speedtest()
                case 'route'|'routes':
                    self._mtr()
                case 'ping'|'pings':
                    self._pingonce()
                case 'sleep5m'|'sleep_5m'|'wait5m':
                    self._sleep_5m()
                case 'sleep10'|'wait10':
                    self._sleep_10()
                case 'sleep60'|'wait60'|'sleep1m'|'wait1m':
                    self._sleep_60()

    
    def do_set(self, user_input):
        ''' set for properties target,targets '''
        actions = user_input.split()
        if(len(actions) == 0):
            self.logger.error("do_set: no actions specified")
            print("No actions specified..")
            return
        action = actions.pop(0)
        match action:
            case 'target'|'targets':
                msg = "Targets cleared and reset via set"
                self.logger.debug(msg)
                print(msg)
                _targs = []
                for t in actions:
                    print("adding target {}".format(t))
                    _targs.append(t)
                self._TARGETS = _targs.copy()
                msg = "set: TARGETS len: {}".format(len(self._TARGETS))
                self.logger.info(msg)
            case default:
                msg = "Attempted to set unknown property {} to val {}".format(action, actions)
                self.logger.debug(msg)
                print(msg)

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
                    msg = "Can't get unknown property {}".format(p)
                    self.logger.debug(msg)
                    print(msg)

    def do_open_targets(self, user_input):
        ''' open targets file and load that into memory'''
        with open(user_input, 'r') as f:
            for entry in f:
                if(len(entry.strip()) > 0): self._TARGETS.append(entry)
        print("Found {} in your targets file!".format(len(self._TARGETS)))

    def do_clear_targets(self, user_input):
        ''' clear target list '''
        self._TARGETS.clear()

    def _speedtest(self):
        ''' run speedtest '''
        tester = speedtest.Speedtest()
        server = tester.get_best_server()
        tester.download()
        tester.upload()
        results_url = tester.results.share()
        results = tester.results.dict()
        rstr = "Speedtest results: {}mbps Down, {}mbps Up, {}ms Latency".format(
                round(results['download']/1024/1024, 0),
                round(results['upload']/1024/1024,0),
                round(results['ping'],1))
        self.logger.info(rstr)
        print(rstr)
        self.logger.info("Speedest Latency: {}ms".format(
            round(results['ping']), 1))
        self.logger.info("Speedtest URL: {}".format(results_url))
        self.logger.info("Speedtest Server Location: {}".format(results['server']['name']))
        self.logger.info("Speedtest Server Host {} by {}".format(
            results['server']['host'], results['server']['sponsor']))
        print("Speedtest completed")

    def _mtr(self):
        ''' run mtr '''
        self._ensure_targets()
        for host in self._TARGETS:
            the_host = host.strip()
            # TODO: add path check for mtr, bolt on traceroute as alternative
            print("Traceroute invoked for {}".format(the_host))
            p_res = subprocess.run(
                    ["mtr","--no-dns","--report-wide","-c","10","--csv", the_host], 
                    capture_output=True)
            _t = StringIO(p_res.stdout.decode()) 
            data = pd.read_csv(_t)
            # delete extraneous data
            del data['Mtr_Version']
            del data['Start_Time']
            data = data.iloc[:, :-1]
            self.logger.info("Traceroute: Info for Host {}".format(host))
            #log the result hop by hop
            for i in data.index:
                msg="Traceroute: Hop# {} IP {} Loss {}% Avg Resp {}ms".format(
                    data['Hop'][i],
                    data['Ip'][i],
                    data['Loss%'][i],
                    data['Avg'][i])
                self.logger.info(msg)
                print(msg)
        
        print("Traceroute completed")

    def _pingonce(self):
        ''' run ping once against targets '''
        self._ensure_targets()
        for host in self._TARGETS:
            the_host = host.strip()
            msg = "Sending 10 pings to {}".format(the_host)
            self.logger.info(msg)
            print(msg)
            ping_result = subprocess.run(
                    ["ping","-c","10","-i","1","-n","-q", the_host],
                    capture_output=True)
            _y = StringIO(ping_result.stdout.decode())
            _x = _y.getvalue().split("\n")
            msg = "PING: {}\nPING: {}".format(_x[-3], _x[-2])
            self.logger.info(msg)
            print(msg)

    
    def _ensure_targets(self):
        if(len(self._TARGETS) == 0):
            self.logger.error("Targets file is empty!")
            self.logger.error("ensure_targets: adding 1.1.1.1")
            self._TARGETS.append("1.1.1.1")
        else:
            self.logger.info("ensure_targets: valid targets exist")
if __name__ == '__main__':
    nms_interactive().cmdloop()
