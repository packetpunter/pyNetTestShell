
from dataclasses import dataclass
from ipaddress import ip_network
from re import search
import dns.resolver
from dns.exception import DNSException

@dataclass
class ValidAddress(str):
    validated_ip = ""

    def __init__(self, input_address="127.0.0.1"):
        if input_address == "127.0.0.1":
            print("setting default IP to localhost")
            self.validated_ip = input_address
        else:
            try:
                _temp_target = ip_network(input_address)
                if(_temp_target.prefixlen == 32): self.validated_ip = _temp_target.network_address
                else:
                    _t = _temp_target.network_address + 2
                    print(f"Target is network. Targeting {_t}")
                    self.validated_ip = _t
            except ValueError as v:
                if("host bits" in repr(v)):
                    print(f"IP was for a CIDR. Must be single host only! Skipping {input_address}!")
                
                if("does not appear to be" in repr(v)):
                    # source oreilly
                    # source url https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch08s15.html
                    domain_regex = "\A([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}\Z"
                    match_result = search(domain_regex, input_address)
                    if match_result:
                        real_result = match_result.string
                        try:
                            dns_response = dns.resolver.resolve(real_result, "A")
                            # source https://stackoverflow.com/questions/49509431/returning-a-dns-record-in-dnspython
                            resolved_ip = "".join([str(dns_response[0], ), ""])
                            self.validated_ip = resolved_ip
                        except DNSException as e:
                            print(f"{e}")       
                else:
                    print(f"Invalid target {input_address}, setting to 127.0.0.1")
            finally:
                if self.validated_ip == "":
                    print(f"Invalid target {input_address}, setting to localhost")
                    self.validated_ip = "127.0.0.1"
                if self.validated_ip == "0.0.0.0":
                    print(f"DNS returned an invalid response for {input_address},\n returning address 0.0.0.0..\nThis is likely a network security block.\nSetting to localhost")
                    self.validated_ip = "127.0.0.1"

    def __repr__(self):
        return self.validated_ip



