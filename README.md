# pyNetTestShell
An interactive python shell to test the network using external commands as well as some python libs for network performance

## Requirements
Please have mtr installed and in the path of the user running the script.

[A medium post on how to install mtr via brew on macos](https://medium.com/macos-sh/mtr-my-traceroute-replacement-7827bd8efa42)

For Windows, I recommend running WSL2 with Ubuntu, then installing and running mtr + this script from there.

[Installing Ubuntu on WSL2 on Windows 10](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview)

## Behavior
The app is interactive, and upon launch, creates a new logfile. 

The logfile is located in ```output/$YEAR/$MONTH/$DAY``` and the file is named according to data in ```Config.py```, using the timestamp for the file name.


## Usage
First preparation
```bash
python3 -m pip install venv
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
```
Running thereafter
```bash
source venv/bin/activate
python shell.py
```

### Sample 
```bash
~/code/pyNetTestShell (main*) » python shell.py 
Welcome to the Network Tester Interactive v1.0 app to test your network!

Type ? to list commands.
 For questions, please contact the administrator who granted you this access.


net_test> set targets 1.1.1.1
Targets cleared and reset via set
adding target 1.1.1.1
net_test> run all
Speedtest results: 436.0mbps Down, 41.0mbps Up, 32.5ms Latency
Speedtest completed
Traceroute invoked for 1.1.1.1
Traceroute completed
net_test> show logfile
/home/me/code/pyNetTestShell/output/2022/12/21/net_test_sessionat_14:49.nmsLog
net_test> open_targets targets.csv
Found 5 in your targets file!
net_test> show targets
['1.1.1.1', '10.3.32.10\n', '10.3.33.10\n', '10.2.19.10\n', '1.1.1.1\n']
net_test> run route
Traceroute invoked for 1.1.1.1
Traceroute invoked for 10.3.32.10
Traceroute invoked for 10.3.33.10
Traceroute invoked for 10.2.19.10
Traceroute invoked for 1.1.1.1
Traceroute completed
net_test> exit
~/code/pyNetTestShell (main*) » cat /home/me/code/pyNetTestShell/output/2022/12/21/net_test_sessionat_14:49.nmsLog
2022-12-21-T-02:49:40 PM::net_test::INFO: set: TARGETS len: 1
2022-12-21-T-02:50:02 PM::net_test::INFO: Speedtest results: 436.0mbps Down, 41.0mbps Up, 32.5ms Latency
2022-12-21-T-02:50:02 PM::net_test::INFO: Speedest Latency: 32ms
2022-12-21-T-02:50:02 PM::net_test::INFO: Speedtest URL: http://www.speedtest.net/result/14105766278.png
2022-12-21-T-02:50:02 PM::net_test::INFO: Speedtest Server Location: Albuquerque, NM
2022-12-21-T-02:50:02 PM::net_test::INFO: Speedtest Server Host stosat-albq-01.sys.comcast.net:8080 by Comcast
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Info for Host 1.1.1.1
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 1 IP 172.26.128.1 Loss 0.0% Avg Resp 0.45ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 2 IP 10.2.0.1 Loss 0.0% Avg Resp 1.15ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 3 IP 75.146.143.206 Loss 0.0% Avg Resp 3.16ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 4 IP 100.92.204.131 Loss 0.0% Avg Resp 13.07ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 5 IP 96.216.21.45 Loss 0.0% Avg Resp 12.9ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 6 IP 68.86.182.121 Loss 0.0% Avg Resp 13.9ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 7 IP 68.85.65.89 Loss 0.0% Avg Resp 13.54ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 8 IP 96.108.43.101 Loss 0.0% Avg Resp 14.04ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 9 IP 96.110.44.25 Loss 0.0% Avg Resp 23.22ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 10 IP 96.110.39.122 Loss 0.0% Avg Resp 21.52ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 11 IP 96.110.39.9 Loss 40.0% Avg Resp 23.67ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 12 IP 96.110.37.241 Loss 0.0% Avg Resp 21.57ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 13 IP 96.110.33.130 Loss 0.0% Avg Resp 23.26ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 14 IP 71.25.197.110 Loss 30.0% Avg Resp 31.76ms
2022-12-21-T-02:50:18 PM::net_test::INFO: Traceroute: Hop# 15 IP 1.1.1.1 Loss 0.0% Avg Resp 22.38ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Info for Host 1.1.1.1
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 1 IP 172.26.128.1 Loss 0.0% Avg Resp 0.24ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 2 IP 10.2.0.1 Loss 0.0% Avg Resp 1.29ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 3 IP 75.146.143.206 Loss 0.0% Avg Resp 3.0ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 4 IP 100.92.204.131 Loss 0.0% Avg Resp 13.35ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 5 IP 96.216.21.45 Loss 0.0% Avg Resp 12.3ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 6 IP 68.86.182.121 Loss 0.0% Avg Resp 12.41ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 7 IP 68.85.65.89 Loss 0.0% Avg Resp 13.26ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 8 IP 96.108.43.101 Loss 0.0% Avg Resp 13.93ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 9 IP 96.110.44.25 Loss 0.0% Avg Resp 21.95ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 10 IP 96.110.39.122 Loss 0.0% Avg Resp 20.43ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 11 IP 96.110.39.9 Loss 50.0% Avg Resp 23.14ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 12 IP 96.110.37.241 Loss 0.0% Avg Resp 21.79ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 13 IP 96.110.33.130 Loss 0.0% Avg Resp 22.01ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 14 IP 71.25.197.110 Loss 30.0% Avg Resp 21.45ms
2022-12-21-T-02:51:55 PM::net_test::INFO: Traceroute: Hop# 15 IP 1.1.1.1 Loss 0.0% Avg Resp 23.96ms
2022-12-21-T-02:52:11 PM::net_test::INFO: Traceroute: Info for Host 10.3.32.10

2022-12-21-T-02:52:11 PM::net_test::INFO: Traceroute: Hop# 1 IP 172.26.128.1 Loss 0.0% Avg Resp 0.34ms
2022-12-21-T-02:52:11 PM::net_test::INFO: Traceroute: Hop# 2 IP 10.2.0.1 Loss 0.0% Avg Resp 1.5ms
2022-12-21-T-02:52:11 PM::net_test::INFO: Traceroute: Hop# 3 IP 75.146.143.206 Loss 0.0% Avg Resp 2.9ms
2022-12-21-T-02:52:11 PM::net_test::INFO: Traceroute: Hop# 4 IP ??? Loss 100.0% Avg Resp 0.0ms
2022-12-21-T-02:52:27 PM::net_test::INFO: Traceroute: Info for Host 10.3.33.10

2022-12-21-T-02:52:27 PM::net_test::INFO: Traceroute: Hop# 1 IP 172.26.128.1 Loss 0.0% Avg Resp 0.49ms
2022-12-21-T-02:52:27 PM::net_test::INFO: Traceroute: Hop# 2 IP 10.2.0.1 Loss 0.0% Avg Resp 1.35ms
2022-12-21-T-02:52:27 PM::net_test::INFO: Traceroute: Hop# 3 IP 75.146.143.206 Loss 0.0% Avg Resp 3.08ms
2022-12-21-T-02:52:27 PM::net_test::INFO: Traceroute: Hop# 4 IP ??? Loss 100.0% Avg Resp 0.0ms
2022-12-21-T-02:52:43 PM::net_test::INFO: Traceroute: Info for Host 10.2.19.10

2022-12-21-T-02:52:43 PM::net_test::INFO: Traceroute: Hop# 1 IP 172.26.128.1 Loss 0.0% Avg Resp 0.34ms
2022-12-21-T-02:52:43 PM::net_test::INFO: Traceroute: Hop# 2 IP 10.2.0.1 Loss 0.0% Avg Resp 1.3ms
2022-12-21-T-02:52:43 PM::net_test::INFO: Traceroute: Hop# 3 IP 75.146.143.206 Loss 0.0% Avg Resp 2.94ms
2022-12-21-T-02:52:43 PM::net_test::INFO: Traceroute: Hop# 4 IP ??? Loss 100.0% Avg Resp 0.0ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Info for Host 1.1.1.1

2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 1 IP 172.26.128.1 Loss 0.0% Avg Resp 0.47ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 2 IP 10.2.0.1 Loss 0.0% Avg Resp 1.29ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 3 IP 75.146.143.206 Loss 0.0% Avg Resp 3.13ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 4 IP 100.92.204.131 Loss 0.0% Avg Resp 13.07ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 5 IP 96.216.21.45 Loss 0.0% Avg Resp 12.16ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 6 IP 68.86.182.121 Loss 0.0% Avg Resp 14.01ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 7 IP 68.85.65.89 Loss 0.0% Avg Resp 14.6ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 8 IP 96.108.43.101 Loss 0.0% Avg Resp 13.43ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 9 IP 96.110.44.25 Loss 0.0% Avg Resp 23.68ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 10 IP 96.110.39.122 Loss 0.0% Avg Resp 21.66ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 11 IP 96.110.39.9 Loss 90.0% Avg Resp 27.45ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 12 IP 96.110.37.241 Loss 0.0% Avg Resp 22.12ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 13 IP 96.110.33.130 Loss 0.0% Avg Resp 23.02ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 14 IP 71.25.197.110 Loss 20.0% Avg Resp 24.15ms
2022-12-21-T-02:52:58 PM::net_test::INFO: Traceroute: Hop# 15 IP 1.1.1.1 Loss 0.0% Avg Resp 22.7ms

```
