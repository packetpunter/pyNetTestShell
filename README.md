# pyNetTestShell
An interactive python shell to test the network using external commands as well as some python libs for network performance

## Requirements
Please have mtr installed and in the path of the user running the script.
[A medium post on how to install mtr via brew on macos](https://medium.com/macos-sh/mtr-my-traceroute-replacement-7827bd8efa42)
[Installing Ubuntu on WSL2 on Windows 10](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview)

## Usage
```bash
python3 -m pip install venv
python3 -m venv venv/
source venv/bin/activate
pip install -r requirements.txt
python shell.py
```
