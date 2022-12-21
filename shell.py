from cmd import Cmd
import Config

class nms_interactive(Cmd):
    prompt = Config._PROGRAM_SLUG + "> "
    intro = "Welcome to the {} v{} app to test your network!\n\n" \
            "Type ? to list commands.\n For questions, please "\
            "contact the administrator who granted you this access.\n\n".format(
                    Config._PROGRAM_NAME,
                    Config._VERSION)
    _TARGETS = []
    from datetime import datetime
    import os
    _cwd = os.getcwd()
    _now = datetime.now()
    _fday = _now.strftime("%Y/%m/%d")
    _ftime = _now.strftime("%H:%M")
    _path = _cwd + "/output/" + _fday + "/" 
    
    os.makedirs(_path, exist_ok=True)
    
    _LOGFILE = _path + Config._PROGRAM_SLUG + "_sessionat_" + _ftime + ".nmsLog"
    
    import logging
    logger = logging.getLogger(Config._PROGRAM_SLUG)
    logger.setLevel(logging.DEBUG)

    logfileHandle = logging.FileHandler(_LOGFILE)
    logfileHandle.setLevel(logging.INFO)
    
    formatter = logging.Formatter("%(asctime)s::%(name)s::%(levelname)s: %(message)s", datefmt="%Y-%m-%d-T-%I:%M:%S %p")
    logfileHandle.setFormatter(formatter)

    logger.addHandler(logfileHandle)

    def do_exit(self, user_input):
        ''' exit '''
        print("Exiting per user..")
        return True

    def do_run(self, verbage):
        ''' execute command based off verbage '''
        actions = verbage.split()
        if(len(actions) == 0):
            self.logger.error("do_run: no actions specified")
            return
        action = actions.pop(0) #take first of user's verbs
        match action:
            case 'all':
                self._speedtest()
                self._mtr()
            case 'speed':
                self._speedtest()
            case 'route':
                self._mtr()
    
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
        import speedtest
        tester = speedtest.Speedtest()
        server = tester.get_best_server()
        tester.download()
        tester.upload()
        results_url = tester.results.share()
        results = tester.results.dict()
        
        self.logger.info("Speedtest results: {} mbps Down, {} mbps Up".format(
            round(results['download']/1024/1024, 0), 
            round(results['upload']/1024/1024, 0)))
        self.logger.info("Speedest Latency: {}ms".format(
            round(results['ping']), 1))
        self.logger.info("Speedtest URL: {}".format(results_url))
        self.logger.info("Speedtest Server Location: {}".format(results['server']['name']))
        self.logger.info("Speedtest Server Host {} by {}".format(
            results['server']['host'], results['server']['sponsor']))
        print("Speedtest completed")

    def _mtr(self):
        ''' run mtr '''
        if(len(self._TARGETS) == 0):
            self.logger.error("traceroute invoked without targets!!"\
            "try set_target, or specify in run")
            print("Traceroute had no targets.. skipping")
            return
        for host in self._TARGETS:
            the_host = host.strip()
            # TODO: add path check for mtr, bolt on traceroute as alternative
            print("Traceroute invoked for {}".format(the_host))
            import subprocess
            p_res = subprocess.run(
                    ["mtr","--no-dns","--report-wide","-c","10","--csv", the_host], 
                    capture_output=True)
            import pandas as pd
            from io import StringIO
            _t = StringIO(p_res.stdout.decode()) 
            data = pd.read_csv(_t)
            # delete extraneous data
            del data['Mtr_Version']
            del data['Start_Time']
            data = data.iloc[:, :-1]
            self.logger.info("Traceroute: Info for Host {}".format(host))
            #log the result hop by hop
            for i in data.index:
                self.logger.info("Traceroute: Hop# {} IP {} Loss {}% Avg Resp {}ms".format(
                    data['Hop'][i],
                    data['Ip'][i],
                    data['Loss%'][i],
                    data['Avg'][i]
                    )
                )
        
        print("Traceroute completed")


if __name__ == '__main__':
    nms_interactive().cmdloop()
