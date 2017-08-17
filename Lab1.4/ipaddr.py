from random import randrange
from ipaddress import IPv4Network

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        net = str(randrange(11,224))+'.0.0.0'
        mask = str(randrange(8,25))
        address = net+'/'+mask
        IPv4Network.__init__(self, address)

    def key_value(self):
        return (self.netmask._ip, self.network_address._ip)


l = []
for i in range(50):
    l.append(IPv4RandomNetwork())

l.sort(key=lambda net: net.key_value())

for network in l:
    print(network)
