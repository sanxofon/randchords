# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:03:42 2016

@author: Santiago Chávez
"""

import re

def midiStr2Int(nota):
	Notez = {"C":0,"Db":1,"D":2,"Eb":3,"E":4,"F":5,"Gb":6,"G":7,"Ab":8,"A":9,"Bb":10,"B":11}
	return Notez[nota]

strChords = """C [0, 4, 7] [M]
D [0, 3, 7] [m]
E [0, 3, 7] [m]
F [0, 4, 7] [M]
G [0, 4, 7] [M]
A [0, 3, 7] [m]
B [0, 3, 6] [dim]"""

# Clean strChords
strChords = re.sub('/\r/u','',strChords)
strChords = re.sub('/  +/u',' ',strChords)
strChords = re.sub('/\n\n+/u','\n',strChords)

# Split it to a list
lstChords = []
for c in strChords.split("\n"):
    c = c.strip().split('[')
    lstChords.append([c[0].strip(),[int(x.strip()) for x in c[1].strip(' ],').split(',')], midiStr2Int(c[0].strip()), [int(x.strip())+midiStr2Int(c[0].strip()) for x in c[1].strip(' ],').split(',')]])

print lstChords
