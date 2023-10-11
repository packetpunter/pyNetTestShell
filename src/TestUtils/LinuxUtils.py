import subprocess
from io import StringIO

class os_runner:
    ''' run cmd_str in os '''
    def __init__(self, args):
        self._cmd = []
        for cmd_data in args.split(" "):
            self._cmd.append(cmd_data)
        self._run(self._cmd)
    
    def _run(self, command_data) -> str:        
        output = subprocess.run(command_data, capture_output=True)
        data = StringIO(output.stdout.decode())
        print(data.read())
        self._output = data
        data.close()

def is_linux() -> bool:
    """ returns false if this is not running on linux"""
    # TODO: convert to decorator
    from sys import platform

    match platform:
        case 'linux':
            return True
        case _:
            print(f"Commands on {platform} operating systems are unsupported. Failed.")
            return False

    
def sudo_whoami():
    if is_linux():
        os_runner("sudo whoami")

def linux_repo_install():
    if is_linux():
        os_runner("sudo apt -y install iperf3")

def linux_manual_install():
    if is_linux():
        os_runner("sudo wget -O /usr/lib/libiperf.so.0 https://iperf.fr/download/ubuntu/libiperf.so.0_3.1.3")
        os_runner("sudo wget -O /usr/bin/iperf3 https://iperf.fr/download/ubuntu/iperf3_3.1.3")
        os_runner("sudo chmod +x /usr/bin/iperf3")
