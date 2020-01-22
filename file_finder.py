#this program checks whats under the given file path

import os

path = 'D:\Kortti\MyPythonScripts'

for folderName, subfolders, filenames in os.walk(path):
        print('The folder is ' + folderName)
        print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
        print('The filenames in ' + folderName + ' are: ' + str(filenames))
        print()

 
