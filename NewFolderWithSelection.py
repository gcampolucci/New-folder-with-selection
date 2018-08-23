#! /usr/bin/python3 -OOt
import sys
import os
import shutil


# Empty list
sel_files = []

# Insert selected files into list
for i in sys.argv[1:]:
    sel_files.append(i)

# Selected files common path
commonPath = os.path.commonpath(sel_files)
# New folder name
newFolder = "New Folder with items"
# New directory
commonPath = os.path.join(commonPath,newFolder)

# Counter
x = 1
# Counter --string format for directory name
s = ""

# If exist:
#  New Folder with items
#  New Folder with items (2)
#  New Folder with items (3)
while os.path.isdir(commonPath + s):
    x = x + 1
    s = " (" + str(x) + ")"
else:
    # new directory 
    os.makedirs(commonPath + s)
    # moving selected files into new directory
    for i in sel_files:
        shutil.move(i, commonPath + s)
