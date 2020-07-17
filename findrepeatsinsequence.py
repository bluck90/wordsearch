# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:07:16 2020

@author: btgl1e14
"""

numberlist = [6,2,4,3,7,5,3,2,4,1,8,3,3,4,5,8,9,4,5,3,2,5,4,6,8,2,2,4,4,3,5,1,3,1,2,6,9,8,6,7,5,6,3,4,6,5,5,7,7,4,2,3,8,9,7,8,3,3,4,5,8,7,6,9,8,7,6,8,3,3,4,5,7]
n = 6
import pandas as pd 


chakra1 = pd.read_csv('chakra1.csv', header=None)
chakra2 = pd.read_csv('chakra2.csv', header=None)
twochakra1 = pd.read_csv('2chakra1.csv', header=None)
chakra8_11 = pd.read_csv('chakra8_11.csv', header=None)

import numpy as np

# Searches list to determine how many times small list is included in big list
def contains(small, big):
    counter = 0
    # initiating list of indexes. N.B. indexlist gives LAST index of sequence, not first
    indexlist = []
    for i in range(len(big)-len(small)+1):
        for j in range(len(small)):
            if big[i+j] != small[j]:
                break
        else:
            counter += 1
            indexlist.append(i+j)
    if counter > 0:
        return counter, indexlist
    return False

def findrepeats(sequence, n_letters):
    fulldict = {}
    # Iterating through all the short-sequences of n letters in the list
    for i in range(0, len(sequence) - n_letters):
        shortliststr = ""
        shortlist = sequence[i:i + n_letters]
        for number in shortlist:
            shortliststr = shortliststr + "." + str(number)
        # If short-sequence is found in full sequence more than once (i.e. itself), add to dict
        if contains(shortlist, sequence)[0] > 1 and len(shortlist) == n_letters:
            fulldict[shortliststr] = contains(shortlist, sequence)
    return fulldict

def findallrepeats(sequence, min_letters, max_letters):
    fulldict = {}
    # Iterating through all possible n_letters in findrepeats() between given range
    for i in range(min_letters, max_letters):
        newdict = findrepeats(sequence, i)
        fulldict.update(newdict)
    return fulldict



def chakradown(chakra): 
    # Create an empty list 
    row_list =[]  
    # Iterate over each row 
    for index, rows in chakra.iterrows(): 
        # Create list for the current row 
        for number in rows:
            row_list.append(number)
        # append the list to the final list 
    return row_list
  
def chakraright(chakra):
    # Create an empty list 
    col_list = []  
    # Iterate over each row 
    for index, columns in chakra.iteritems(): 
        # Create list for the current row 
        for number in columns:
            col_list.append(number)
        # append the list to the final list 
    return col_list
    
        
        
# diagonal coords
def diagonal_coords_up_right(wordsearch):
    height = len(wordsearch)
    width = len(wordsearch[0])
    maxlength = min(height, width)
    vector = [1,1]
    allcoords = []
    for h in range(0, height):
        coords = []
        coord = np.array([h,0])
        for j in range(0, maxlength):
            if coord[0] > height - 1:
                continue
            coords.append(coord)
            coord = np.add(coord, vector)
        allcoords.append(coords)    
    for i in range(0, width):
        coords = []
        coord = np.array([0,i])
        for j in range(0, maxlength):
            if coord[1] > width - 1:
                continue
            coords.append(coord)
            coord = np.add(coord, vector)
        allcoords.append(coords)   
    return allcoords

def diagonal_coords_up_left(wordsearch):
    height = len(wordsearch)
    width = len(wordsearch[0])
    vector = [1,-1]
    maxlength = min(height, width)
    allcoords = []
    for h in range(0, height):
        coords = []
        coord = np.array([h,width-1])
        for j in range(0, maxlength):
            if coord[0] > height - 1:
                continue
            coords.append(coord)
            coord = np.add(coord, vector)
        allcoords.append(coords)    
    for i in range(0, width):
        coords = []
        coord = np.array([0,i])
        for j in range(0, maxlength):
            if coord[1] < 0:
                continue
            coords.append(coord)
            coord = np.add(coord, vector)
        allcoords.append(coords)  
    return allcoords

# Getting list of strings from coords
def strings_from_coords(wordsearch, coords):
    strings = []
    for stringcoords in coords:
        for lettercoords in stringcoords:
            letter = wordsearch[lettercoords[0]][lettercoords[1]]
            strings.append(letter)
    return strings

# diagonal strings
def diagonal_strings_up_right(wordsearch):
    coords = diagonal_coords_up_right(wordsearch)
    strings = strings_from_coords(wordsearch, coords)
    return strings

def diagonal_strings_up_left(wordsearch):
    coords = diagonal_coords_up_left(wordsearch)
    strings = strings_from_coords(wordsearch, coords)
    return strings

c8_11down = chakradown(chakra8_11)
c8_11right =  chakraright(chakra8_11)
c8_11ur = diagonal_strings_up_right(chakra8_11)
c8_11ul = diagonal_strings_up_left(chakra8_11)


width = len(chakra1)
height = len(chakra1[0])
diag_list = []
vector = [1, -1]


c8_11ured = {key:val for key, val in c8_11_ur.items() if val[0] != 2}
c8_11uled = {key:val for key, val in c8_11_ul.items() if val[0] != 2}
longdicted = {key:val for key, val in longdict.items() if val[0] != 2}

def doalldirections(down, right, ul, ur, min_letters, max_letters):
    dict1 = findallrepeats(down, min_letters, max_letters)
    dict2 = findallrepeats(right, min_letters, max_letters)
    dict3 = findallrepeats(ul, min_letters, max_letters)
    dict4 = findallrepeats(ur, min_letters, max_letters)
    return dict1, dict2, dict3, dict4

def alldirections(chakra, min_letters, max_letters):
    down = chakradown(chakra)
    right = chakraright(chakra)
    ul = diagonal_strings_up_left(chakra)
    ur = diagonal_strings_up_right(chakra)
    dict1 = findallrepeats(down, min_letters, max_letters)
    dict2 = findallrepeats(right, min_letters, max_letters)
    dict3a = findallrepeats(ul, min_letters, max_letters)
    dict4a = findallrepeats(ur, min_letters, max_letters)
    dict3 = {key:val for key, val in dict3a.items() if val[0] != 2}
    dict4 = {key:val for key, val in dict4a.items() if val[0] != 2}
    return dict1, dict2, dict3, dict4

dict_down, dict_right, dict_ul, dict_ur = alldirections(chakra8_11, 6, 14)

c8_11_down, c8_11_right, c8_11_ul, c8_11_ur = doalldirections(c8_11down,c8_11right,c8_11ul,c8_11ur,4,11)

longlist = []
longlist.extend(c8_11ul)
longlist.extend(twoul1_list)
longlist.extend(ul)
longlist.extend(ul2_list)

longdict = findallrepeats(longlist, 5,17)
