from io import StringIO
import subprocess
from TestUtils.TestResults import TestResult

def ping_runner(targetList):
    _TARGETS = targetList
    results = _pinger(_TARGETS)
    return results

def _pinger(targets) -> TestResult:
    msgs = []
    for host in targets:
        the_host = host.strip()
        ping_result = subprocess.run(
                ["ping","-c","10","-i","1","-n","-q", the_host],
                capture_output=True)
        ping_lines = StringIO(ping_result.stdout.decode()).getvalue().split()
        t_names = ping_lines[-4].split("/")
        t_vals = ping_lines[-2].split("/")
        
        for name in t_names:
            nameIdx = t_names.index(name)
            new_name = ""
            match(name):
                case "min":
                    new_name = "TR_Ping_Min"
                case "avg":
                    new_name = "TR_Ping_Avg"
                case "max":
                    new_name = "TR_Ping_Max"
                case "mdev":
                    new_name = "TR_Ping_StdDev"
            t_names.remove(name)
            t_names.insert(nameIdx, new_name)
        
        t_names.append("TR_Ping_PctLoss")
        t_vals.append(ping_lines[10])

        rl = dict(zip(t_names, t_vals))
        
        # TODO: move this into the TestResult class
        result_frame = TestResult("ping")._frame
        result_frame["TA_SRC"] = "self"
        result_frame["TA_DST"] = the_host
        result_frame["TR_Ping_Min"] = rl["TR_Ping_Min"]
        result_frame["TR_Ping_Max"] = rl["TR_Ping_Max"]
        result_frame["TR_Ping_Min"] = rl["TR_Ping_Avg"]
        result_frame["TR_Ping_StdDev"] = rl["TR_Ping_StdDev"]
        result_frame["TR_Ping_PctLoss"] = rl["TR_Ping_PctLoss"]

        msgs.append(f"PING: Pinging host {the_host}\n")
        msgs.append("PING: {} {}\n".format(_x[-3], _x[-2]))
        return msgs