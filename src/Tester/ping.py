from io import StringIO
import subprocess

def ping_runner(targetList):
    _TARGETS = targetList
    results = _pinger(_TARGETS)
    return results

def _pinger(targets):
    msgs = []
    for host in targets:
        the_host = host.strip()
        ping_result = subprocess.run(
                ["ping","-c","10","-i","1","-n","-q", the_host],
                capture_output=True)
        _y = StringIO(ping_result.stdout.decode())
        _x = _y.getvalue().split("\n")
        msgs.append(f"PING: Pinging host {the_host}\n")
        msgs.append("PING: {} {}\n".format(_x[-3], _x[-2]))
        return msgs