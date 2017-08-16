from random import randrange
from ipaddress import IPv4Network

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        net = str(randrange(11,224))+'.0.0.0'
        mask = str(randrange(8,25))
        address = net+'/'+mask
        IPv4Network.__init__(self, address)

    def key_value(self):
        return (self.network_address._ip, self.netmask._ip)


