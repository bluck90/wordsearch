# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:43:22 2020

@author: btgl1e14
"""

wordsearch = 'doggo oogod gogdg oodgo dgood ododg ggodo'

matrix = wordsearch.split()
height = len(matrix)
width = len(matrix[0])

horizontal1 = ''
for i in range(0, height + 1):
    for j in range(0, width + 1):
        print(j)
        

for word in reversed(matrix):
    print(word)

for i, row in enumerate(matrix):
    for j, letter in enumerate(row):
        string = 


st = ["doggo", "oogod", "godgo"]
strin = 'dogg'


# this works for a list of strings
all_words = {st[h][i:j + i] for h in range(0,len(st)) for j in range(3,len(st[h])+1) for i in range(0, (len(st[h])+1)-j)}



# this allwords works, finally
allwordsmine = {strin[i:j+i] for j in range(3,len(strin)+1) for i in range(0, (len(strin)+1)-j)}

# allwords forwards for list
allwordsmineall = {st[h][i:j+i] for h in range(0, len(st)) for j in range(3,len(st[h])+1) for i in range(0, (len(st[h])+1)-j)}

# list of strings backwards (forwards reversed)
backwards = [st[h][::-1] for h in range(0, len(st))]

#allwords backwards for list
allwordsmineallbackwards = {backwards[h][i:j+i] for h in range(0, len(backwards)) for j in range(3,len(backwards[h])+1) for i in range(0, (len(backwards[h])+1)-j)}

#combining sets
fullset = allwordsmineall|allwordsmineallbackwards

# list of strings upwards
upwards = []
h = 0
for i in range(0, len(st[h])):
    astring = ''
    for h in range(0, len(st)):
        aletter = st[h][i]
        astring = astring + aletter
    upwards.append(astring)

def upwards_strings(wordsearch):
    strings = []
    h = 0
    for i in range(0, len(wordsearch[h])):
        string = ''
        for h in range(0, len(wordsearch)):
            letter = wordsearch[h][i]
            string = string + letter
        strings.append(string)
    return strings


# list of strings downwards (upwards reversed)
downwards = [upwards[h][::-1] for h in range(0, len(upwards))]

# Alternative way to do downwards, redundant
"""
downwards = []
h = len(st)-1
for i in range(0, len(st[h])):
    astring = ''
    for h in range(len(st)-1,-1,-1):
        aletter = st[h][i]
        astring = astring + aletter
    downwards.append(astring)
"""

# DIAGONALS
# Up-Right
# Need numpy for my vector array addition
import numpy as np

# This gives all diagonal coords up-right, first loop is all diags starting along the left side, second all starting along the bottom side
height = len(st)
width = len(st[0])
vector = [1,1]
maxlength = min(height, width)
allcoordsupright = []
for h in range(0, height):
    coords = []
    coord = np.array([h,0])
    for j in range(0, maxlength):
        if coord[0] > height - 1:
            continue
        coords.append(coord)
        coord = np.add(coord, vector)
    allcoordsupright.append(coords)    
for i in range(0, width):
    coords = []
    coord = np.array([0,i])
    for j in range(0, maxlength):
        if coord[1] > width - 1:
            continue
        coords.append(coord)
        coord = np.add(coord, vector)
    allcoordsupright.append(coords)

# Up-left
height = len(st)
width = len(st[0])
vector = [1,-1]
maxlength = min(height, width)
allcoordsupleft = []
for h in range(0, height):
    coords = []
    coord = np.array([h,width-1])
    for j in range(0, maxlength):
        if coord[0] > height - 1:
            continue
        coords.append(coord)
        coord = np.add(coord, vector)
    allcoordsupleft.append(coords)    
for i in range(0, width):
    coords = []
    coord = np.array([0,i])
    for j in range(0, maxlength):
        if coord[1] < 0:
            continue
        coords.append(coord)
        coord = np.add(coord, vector)
    allcoordsupleft.append(coords)

# Getting list of strings from diagonal coords
words = []
for wordcoords in allcoordsupright:
    word = ''
    for lettercoords in wordcoords:
        uprightletter = st[lettercoords[0]][lettercoords[1]]
        word = word + uprightletter
    words.append(word)
    
allwordsminealldiag = {words[h][i:j+i] for h in range(0, len(words)) for j in range(3,len(words[h])+1) for i in range(0, (len(words[h])+1)-j)}

          













range1 = range(1,-1,-1)
for number in range1:
    print(number)

# this loop works
for j in range(3,len(strin)+1):
    for i in range(0, (len(strin)+1)-j):
        print("i = " + str(i) + ", i+j =" + str(i + j))
 # thir loop does not       
for j in range(3, len(strin)):
    for i in range(len(strin)- j + 2):
        print("i = " + str(i) + ", i+j =" + str(i + j))
        