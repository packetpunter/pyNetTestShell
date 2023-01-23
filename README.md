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

### Installation

First preparation

```bash
python3 -m pip install pyNetTestShell-2.0a0-py3-none-any.whl
```
### Usage
This application has two ways to interface with it. There is an interactive shell called net_test, and an execuble for one time testing.

#### Interactive Shell
```bash
python3 -m TestShell

```
##### Sample Output
```bash
Welcome to the Network Tester Interactive v2.0a0 app to test your network!

Type ? to list commands.
 For questions, please contact the administrator who granted you this access.


net_test> set targets 10.2.0.1 10.2.0.250
Targets cleared and reset via set
adding target 10.2.0.1
adding target 10.2.0.250
net_test> run ping sleep10 route sleep60 ping
Sending 10 pings to 10.2.0.1
PING: 10 packets transmitted, 10 received, 0% packet loss, time 9013ms
PING: rtt min/avg/max/mdev = 1.120/1.523/3.250/0.603 ms
Sending 10 pings to 10.2.0.250
PING: 10 packets transmitted, 10 received, 0% packet loss, time 9298ms
PING: rtt min/avg/max/mdev = 0.600/0.838/1.351/0.195 ms
Sleeping for 10 seconds
Traceroute invoked for 10.2.0.1
Traceroute: Hop# 1 IP 172.22.96.1 Loss 0.0% Avg Resp 0.35ms
Traceroute: Hop# 2 IP 10.2.0.1 Loss 0.0% Avg Resp 1.48ms
Traceroute invoked for 10.2.0.250
Traceroute: Hop# 1 IP 172.22.96.1 Loss 0.0% Avg Resp 0.4ms
Traceroute: Hop# 2 IP 10.2.0.250 Loss 0.0% Avg Resp 0.82ms
Traceroute completed
Sleeping for 1 minute
Sending 10 pings to 10.2.0.1
PING: 10 packets transmitted, 10 received, 0% packet loss, time 9014ms
PING: rtt min/avg/max/mdev = 1.000/1.340/1.664/0.205 ms
Sending 10 pings to 10.2.0.250
PING: 10 packets transmitted, 10 received, 0% packet loss, time 9399ms
PING: rtt min/avg/max/mdev = 0.480/0.827/1.209/0.205 ms
net_test>exit
```

#### One Off Execution

```bash
python3 -m Flamegrid test run -i google.com,reddit.com -t ping,route
```

##### Sample Output
```bash
Spawning Tester with Test route against host set [142.250.72.78, 151.101.193.140]
TestSession: Validated target google.com
TestSession: Validated target reddit.com
TestSession: Begin route testing
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 1 IP 10.2.0.1 Loss 0.0% Avg Resp 0.85ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 2 IP 75.146.143.206 Loss 0.0% Avg Resp 2.56ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 3 IP 100.92.204.131 Loss 0.0% Avg Resp 12.29ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 4 IP 96.216.21.45 Loss 0.0% Avg Resp 11.62ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 5 IP 68.86.182.121 Loss 0.0% Avg Resp 11.98ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 6 IP 68.85.65.89 Loss 0.0% Avg Resp 12.49ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 7 IP 96.108.43.101 Loss 0.0% Avg Resp 14.04ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 8 IP 96.110.44.21 Loss 0.0% Avg Resp 20.19ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 9 IP 96.110.38.118 Loss 0.0% Avg Resp 21.34ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 10 IP 50.248.118.30 Loss 0.0% Avg Resp 22.84ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 11 IP 108.170.254.65 Loss 0.0% Avg Resp 21.61ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 12 IP 142.251.48.5 Loss 0.0% Avg Resp 22.3ms
TestSession: TEST route:: RESULTS Traceroute against google.com: Hop# 13 IP 142.250.72.78 Loss 0.0% Avg Resp 22.64ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 1 IP 10.2.0.1 Loss 0.0% Avg Resp 0.85ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 2 IP 75.146.143.206 Loss 0.0% Avg Resp 2.42ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 3 IP 100.92.204.130 Loss 0.0% Avg Resp 12.02ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 4 IP 69.139.177.49 Loss 0.0% Avg Resp 13.86ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 5 IP 68.85.65.89 Loss 0.0% Avg Resp 12.83ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 6 IP 96.108.43.101 Loss 0.0% Avg Resp 14.36ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 7 IP 96.110.44.25 Loss 0.0% Avg Resp 22.16ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 8 IP 96.110.39.106 Loss 0.0% Avg Resp 23.16ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 9 IP 96.110.36.205 Loss 0.0% Avg Resp 20.78ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 10 IP 96.110.37.237 Loss 0.0% Avg Resp 21.65ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 11 IP 96.110.33.126 Loss 0.0% Avg Resp 23.08ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 12 IP 173.167.57.202 Loss 0.0% Avg Resp 21.19ms
TestSession: TEST route:: RESULTS Traceroute against reddit.com: Hop# 13 IP 151.101.1.140 Loss 0.0% Avg Resp 23.33ms
Spawning Tester with Test ping against host set [142.250.72.78, 151.101.193.140]
TestSession: Validated target google.com
TestSession: Validated target reddit.com
TestSession: Begin ping tests
TestSession: TEST ping:: RESULTS PING: Pinging host google.com
TestSession: TEST ping:: RESULTS PING: 10 packets transmitted, 10 received, 0% packet loss, time 9014ms rtt min/avg/max/mdev = 19.226/21.745/24.461/1.606 ms
```
