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

