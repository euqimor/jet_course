import glob
from re import search

def strClass(str):
    expIP = '^ *ip +address +(([0-9]\.?)+) +(([0-9]\.?)+)'
    expInt = '^ *interface +(.+)'
    expHost = '^ *hostname +(.+)'
    if bool(search(expIP,str)):
        result = search(expIP,str)
        return ('IP',result.group(1),result.group(3))
    elif bool(search(expInt,str)):
        result = search(expInt,str)
        return ('INT',result.group(1))
    elif bool(search(expHost,str)):
        result = search(expHost,str)
        return ('HOST',result.group(1))
    else:
        return ('UNCLASSIFIED',)

def getPath():
    path = 'C:\\python_local\\projects\\p4ne\Lab1.5\\config_files\\'
    print('Default filepath is: '+path)
    tmp = input('Press Enter to use the default filepath or enter the path manually:')
    if tmp != '':
        path = tmp
    print('\nWorking, please wait...')
    return path

path = getPath()

lTxt = []
while len(lTxt) == 0:
    lTxt = glob.glob(path+'*.txt')
    if len(lTxt) == 0:
        print('\nNo txt files found under the specified path.')
        path = getPath()

strList = []
for filePath in lTxt:
    file = open(filePath)
    for string in file:
        tmp = strClass(string)
        if tmp[0] != 'UNCLASSIFIED':
            strList.append(tmp)
    file.close()

def areYouSure():
    print('\nThe resulting list is '+str(len(strList))+' long.')
    answer = input('Are you sure you want to print it? [Y/N]')
    while True:
        if answer == 'Y' or answer == 'y':
            print('\n')
            for entry in strList:
                print(entry)
            break
        elif answer == 'N' or answer == 'n':
            print('\nWise choice!')
            break
        else:
            answer = input('Please answer Y or N:')

if __name__=='__main__':
    areYouSure()