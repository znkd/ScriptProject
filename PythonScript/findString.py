#!/usr/bin/python3
# How to use?
# python3 findString.py file1 file2

import sys

keyFile = sys.argv[1]
findFromFile = sys.argv[2]
print("\n外部参数：",keyFile,"&",findFromFile)

class FindManager:
    allKeysArray = []
    def getAllKeyFromFile(self, allKeysFile):
        with open(allKeysFile, mode='r') as file:
            allKeysString = file.read()
            self.allKeysArray = allKeysString.split('\n')
        return self.allKeysArray

    def findSingleString(self,keyStringArray, targetFile):
        if len(keyStringArray) == 0 :
            return

        with open(targetFile, mode='r') as file:
            data = file.read()
            filesize = len(data)
            file.seek(0,0)
            for singleKey in keyStringArray:
                print("found the key \""+'\033[34m'+singleKey+'\033[0m'+"\":")
                while file.tell() != filesize:
                    lineString = file.readline()
                    if lineString.find(singleKey) != -1:
                        print('\033[33m'+lineString+'\033[0m')
                file.seek(0,0)
            pass
        pass
        print("end")
    pass

if __name__ == '__main__':
    print("start")
    mgr = FindManager()
    arr = mgr.getAllKeyFromFile(keyFile)
    print(arr)
    mgr.findSingleString(arr,findFromFile)
    pass