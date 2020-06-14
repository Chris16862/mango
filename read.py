import csv
import shutil
import os
dir_root = "/home/chris/Documents/mango/ml-hw/C1-P1_Dev"
dir_A = "/home/chris/Documents/mango/ml-hw/mango_dev/A"
dir_B = "/home/chris/Documents/mango/ml-hw/mango_dev/B"
dir_C = "/home/chris/Documents/mango/ml-hw/mango_dev/C"
A = []
B = []
C = []
print(dir_root)
with open("dev.csv",newline = '') as trainfile:
    rows = csv.reader(trainfile)

    for row in rows:
        if row[1]=='A':
            A.append(row[0])
        elif row[1]=='B':
            B.append(row[0])
        elif row[1]=='C':
            C.append(row[0])

for name in A:
    for filename in os.listdir(dir_root):
        if filename == name:
            shutil.copy(dir_root+"/"+name,dir_A)

for name in B:
    for filename in os.listdir(dir_root):
        if filename == name:
            shutil.copy(dir_root+"/"+name,dir_B)

for name in C:
    for filename in os.listdir(dir_root):
        if filename == name:
            shutil.copy(dir_root+"/"+name,dir_C)