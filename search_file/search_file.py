# !/usr/bin/env python
#sanoob aboo husain

#usage: ./search_file.py <filepath> <text to search>
# example:  ./search_file.py hospitaldata/ 0013256

import os
import sys


def search_uhid(filepath, text):
    for root, subFolders, files in os.walk(filepath):
        for file in files:
           with open(os.path.join(root, file), 'r') as fin:
            for lines in fin:
                if lines.count(text) > 0:
                    print text+'****** found in ****** ' + file
                    #print file

try:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    search_uhid(arg1, arg2)
except:
    print "Usage: ./search_file.py <File path> <Text to search>"


