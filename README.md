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
Welcome to the Network Tester Interactive v1.21 app to test your network!

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
