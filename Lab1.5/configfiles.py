import glob
from ipaddress import IPv4Network

#lTxt = glob.glob(".\\Lab1.5\\config_files\\*.txt")
# path = 'C:\\python_local\\projects\\p4ne\Lab1.5\\config_files\\'
def getPath():
    path = 'C:\\python_local\\projects\\p4ne\Lab1.5\\config_files\\'
    print('Default filepath is: '+path)
    tmp = input('Press Enter to use the default filepath or enter the path manually:')
    if tmp != '':
        path = tmp
    return path

path = getPath()

lTxt = []
while len(lTxt) == 0:
    lTxt = glob.glob(path+'*.txt')
    if len(lTxt) == 0:
        print('\nNo txt files found under the specified path.')
        path = getPath()

ipList = []
for filePath in lTxt:
    file = open(filePath)
    for string in file:
        strippedString = string.strip()
        if "ip address" in strippedString[:10] and 'dhcp' not in string:
            if strippedString[11:] not in ipList:
                ipList.append(strippedString[11:])
    file.close()

netList = []
for i in range(len(ipList)):
    netList.append(IPv4Network(ipList[i].split(' ')[0]+'/'+ipList[i].split(' ')[1],strict=False))

for net in netList:
    print(net)

# print('List of unique ip addresses:\n')
# for address in ipList:
#     print(address)