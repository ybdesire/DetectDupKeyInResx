#Scan folder & sub-folders and detect all the *.resx files to see if there is any duplicated key definition.
#Usage: configure repoDir and run it. 
#Python 3.4.1

import os
import shutil
import xml.etree.ElementTree as ET

repoDir = "E:\\Resourcefiles\\app\\"  #repository path of source code to be detected

def detectDupKeyAtRes(resFilePath):
    keys=[]
    tree = ET.parse(resFilePath)
    root = tree.getroot()
    for string in root.iter("data"):
        value = string.get("name")
        keys.append(value)
    keys.sort()
    previousAccessKey = ""
    for x in keys:
        if(keys.count(x)>=2 and previousAccessKey!=x):
            print("{} at {}".format(x, resFilePath))
        previousAccessKey = x
			
def main():
    for root,dirs,files in os.walk(repoDir):
        for filesPath in files:
            if os.path.splitext(filesPath)[1] in '.resx':
                detectDupKeyAtRes(root+'\\'+filesPath)

if __name__=="__main__":
    main()
