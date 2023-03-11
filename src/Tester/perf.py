from TestUtils.LinuxUtils import  is_linux
from Tester.oscmd import os_runner

def iperf_runner(outputfile, server_ip, port=5201):
    if is_linux():
        os_runner(f"iperf3 -c {server_ip} -p {port} -J --logfile {outputfile}")

