#file in .txt extension
import os
import os.path as path
import scipy

def getNumber(filePath, pattern):
    data = []
    if '.txt' in filePath:
        file = open(filePath, "rt")
    return data

def writeData(filePath, data, mode):
    rs = False
    f = None
    if path.isfile(filePath):
        f = open(filePath, 'w')
    else:
        f = open(filePath, "x")
    f.writelines(data)
    f.close()
    rs = True
    return rs

print(scipy.__version__)