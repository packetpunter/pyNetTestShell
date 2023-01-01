import pandas as pd
import os
import logging
import subprocess
import speedtest

from cmd import Cmd
from io import StringIO
from time import sleep
from yaml import safe_load
from datetime import datetime

with open('Config.yml', 'r') as config_file:
    _CONFIG = safe_load(config_file)

class nms_interactive(Cmd):
    prompt = _CONFIG['shell']['slug'] + "> "
    intro = "Welcome to the {} v{} app to test your network!\n\n" \
            "Type ? to list commands.\n For questions, please "\
            "contact the administrator who granted you this access.\n\n".format(
                    _CONFIG['shell']['name'],
                    _CONFIG['shell']['version'])
    _TARGETS = []
    _cwd = os.getcwd()
    _now = datetime.now()
    _fday = _now.strftime("%Y/%m/%d")
    _ftime = _now.strftime("%H:%M")
    _path = _cwd + "/output/" + _fday + "/" 
    
    os.makedirs(_path, exist_ok=True)
    
    _LOGFILE = _path + _CONFIG['shell']['slug'] + "_sessionat_" + _ftime + ".nmsLog"
    
    logger = logging.getLogger(_CONFIG['shell']['slug'])
    logger.setLevel(logging.DEBUG)

    logfileHandle = logging.FileHandler(_LOGFILE)
    logfileHandle.setLevel(logging.INFO)
    
    formatter = logging.Formatter("%(asctime)s::%(name)s::%(levelname)s: %(message)s", datefmt="%Y-%m-%d-T-%I:%M:%S %p")
    logfileHandle.setFormatter(formatter)

    logger.addHandler(logfileHandle)

    def _logprint(self, msg):
        ''' print to console and log '''
        print(msg)
        self.logger.info(msg)

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
                case 'sleep1h'|'wait1h':
                    self._sleep_1h()
                case 'sleep30m'|'wait30m':
                    self._sleep_30m()
    
    def do_set(self, user_input):
        ''' set for properties target,targets '''
        actions = user_input.split()
        if(len(actions) == 0):
            self.logprint("do_set: no actions specified")
            return
        action = actions.pop(0)
        match action:
            case 'target'|'targets':
                self._logprint("Targets cleared and reset via set")
                _targs = []
                for t in actions:
                    _targs.append(t)
                self._TARGETS = _targs.copy()
                self.logger.debug("set: TARGETS len: {}".format(len(self._TARGETS)))

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
                if(len(entry.strip()) > 0): self._TARGETS.append(entry)
        self._logprint("Found {} in your targets file!".format(len(self._TARGETS)))

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
        self._logprint(rstr)
        # additional info to logfile
        self.logger.info("Speedest Latency: {}ms".format(
            round(results['ping']), 1))
        self._logprint("Speedtest URL: {}".format(results_url))
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
            self._logprint("Traceroute invoked for {}".format(the_host))
            p_res = subprocess.run(
                    ["mtr","--no-dns","--report-wide","-c","10","--csv", the_host], 
                    capture_output=True)
            _t = StringIO(p_res.stdout.decode()) 
            data = pd.read_csv(_t)
            # delete extraneous data
            del data['Mtr_Version']
            del data['Start_Time']
            data = data.iloc[:, :-1]
            #log the result hop by hop
            for i in data.index:
                msg="Traceroute: Hop# {} IP {} Loss {}% Avg Resp {}ms".format(
                    data['Hop'][i],
                    data['Ip'][i],
                    data['Loss%'][i],
                    data['Avg'][i])
                self._logprint(msg)
        
        print("Traceroute completed")

    def _pingonce(self):
        ''' run ping once against targets '''
        self._ensure_targets()
        for host in self._TARGETS:
            the_host = host.strip()
            self._logprint("Sending 10 pings to {}".format(the_host))
            ping_result = subprocess.run(
                    ["ping","-c","10","-i","1","-n","-q", the_host],
                    capture_output=True)
            _y = StringIO(ping_result.stdout.decode())
            _x = _y.getvalue().split("\n")
            print("PING: {}\nPING: {}".format(_x[-3], _x[-2]))
            # info split into individual log lines
            self.logger.info("PING1:{}".format(_x[-3]))
            self.logger.info("PING2:{}".format(_x[-2]))

    
    def _ensure_targets(self):
        if(len(self._TARGETS) == 0):
            self.logger.error("Targets file is empty!")
            for host in _CONFIG['default']['targets']:
                self.logger.error("ensure_targets: adding {}".format(host))
                self._TARGETS.append(host)
        else:
            self.logger.info("ensure_targets: valid targets exist")


if __name__ == '__main__':
    nms_interactive().cmdloop()
