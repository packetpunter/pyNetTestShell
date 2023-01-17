import subprocess
from io import StringIO
import pandas as pd

def trace_runner(targetList):
    return _mtr(targetList)

def _mtr(targets):
    msgs = []
    for host in targets:
        the_host = host.strip()
        # TODO: add path check for mtr, bolt on traceroute as alternative
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
            msg="Traceroute against {}: Hop# {} IP {} Loss {}% Avg Resp {}ms".format(
                the_host,
                data['Hop'][i],
                data['Ip'][i],
                data['Loss%'][i],
                data['Avg'][i])
            msgs.append(msg)
    return msgs