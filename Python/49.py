from ntpath import join
from os import listdir
from os.path import isfile

directoryItemsList = listdir("/Users/SanketPatil/Downloads")

for directoryItem in directoryItemsList:
    if(isfile(join("/Users/SanketPatil/Downloads/", directoryItem))):
        print(directoryItem)
