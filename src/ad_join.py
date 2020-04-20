#!/usr/bin/env python3

# join two files for the College data set: aaup and usnews

# run as 'ad_join.py > data/combined.dat'

# author: ali dasdan
# date: jun 2019

import csv

# read the first lines from each file for the schemas

# file1: aaup

inpname1 = "data/aaup.dat"
with open(inpname1, 'r') as inpfile:
    aaup = inpfile.readline().strip()

fields1 = aaup.split(',')

# file2: usnews

inpname2 = "data/usnews.dat"
with open(inpname2, 'r') as inpfile:
    usnews = inpfile.readline().strip()

fields2 = usnews.split(',')

fields = fields2[1:] + fields1[4:]
print(",".join(fields))

# join the files using the FICE field

rows = {}

with open(inpname1, newline='') as csvfile:
    reader1 = csv.DictReader(csvfile)
    for row in reader1:
        fice = row['FICE']
        rows[fice] = row

with open(inpname2, newline='') as csvfile:
    reader2 = csv.DictReader(csvfile)

    for row2 in reader2:

        fice = row2['FICE']
        if fice not in rows:
            continue
        row1 = rows[fice]

        s = ""
        sep = ""
        for f in fields2[1:]:
            s += sep + row2[f]
            sep = ","

        for f in fields1[4:]:
            s += sep + row1[f]
            sep = ","

        print(s)

# EOF
