from Tester.oscmd import os_runner

def is_linux() -> bool:
    """ returns false if this is not running on linux"""
    # TODO: convert to decorator
    import os
    match os.uname().sysname:
        case 'Linux':
            return True
        case _:
            print(f"Commands on {os.uname().sysname} operating systems are unsupported. Failing command.")
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
