from pysnmp.hlapi import *

a = nextCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107',161)),
    ContextData(),
    ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
    lexicographicMode=False)

b = getCmd(SnmpEngine(),
    CommunityData('public', mpModel=0),
    UdpTransportTarget(('10.31.70.107',161)),
    ContextData(),
    ObjectType(ObjectIdentity('SNMPv2-MIB','sysDescr',0)))

print('\nSystem version:')
for x in b:
    v = x[3]
    for y in v:
        print(y[1])

print('\n\nInterfaces:')
for x in a:
    v = x[3]
    for y in v:
        print(y[1])

