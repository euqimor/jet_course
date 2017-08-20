import glob, sys, time
from threading import Thread
from re import findall
from ipaddress import IPv4Network as Network, IPv4Interface as Interface

class AnimationThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.isRunning = True
    def run(self):
        while self.isRunning:
            spinAnimation()
    def stop(self):
        self.isRunning = False

def spinAnimation():
    spinner = ['/', '-', '\\', '|']
    for item in spinner:
        sys.stdout.write(item)
        sys.stdout.flush()
        sys.stdout.write('\b')
        time.sleep(0.1)

def getAddr(str):
    expAddr = ('interface +(.+) *\n(.*\n(?!!))* *ip address (([0-9]\.?)*) +(([0-9]\.?)*)')
    result = findall(expAddr,str)
    if result:
        return result
    else:
        return False

def getPath():
    path = 'C:\\python_local\\projects\\p4ne\Lab1.5\\config_files\\'
    print('Default filepath is: '+path)
    tmp = input('Press Enter to use the default filepath or enter the path manually:')
    if tmp != '':
        path = tmp
    return path

def getFileList(path):
    fileList = []
    while len(fileList) == 0:
        fileList = glob.glob(path + '*.txt')
        if len(fileList) == 0:
            print('\nNo txt files found under the specified path.')
            path = getPath()
    return fileList

def getAddressList(fileList):
    addressList = []
    for filePath in fileList:
        with open(filePath) as file:
            data = file.read()
            addresses = getAddr(data)
            if addresses:
                for item in addresses:
                    addressList.append(item)
    return addressList

def areYouSure():
    path = getPath()
    fileList = getFileList(path)
    print('\nWorking, please wait...\n')
    animation = AnimationThread()
    animation.start()
    addressList = getAddressList(fileList)
    animation.stop()
    # sys.stdout.write('\rThe resulting list is ' + str(len(addressList)) + ' items long.')
    print('\rThe resulting list is ' + str(len(addressList)) + ' items long.')
    answer = input('Are you sure you want to print it?[Y]') or 'Y'
    while True:
        if answer == 'Y' or answer == 'y':
            i = 0
            print('\n')
            for entry in addressList:
                i+=1
                print('|{: 4}| {: <15} {: <15}|'.format(i,entry[2],entry[4]))
                print('|'+'_'*4+'|'+'_'*32+'|')
            break
        elif answer == 'N' or answer == 'n':
            print('\nWise choice!')
            break
        else:
            answer = input('Please answer Y or N [Y]:') or 'Y'

areYouSure()