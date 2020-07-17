# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 18:07:16 2020

@author: btgl1e14
"""

#big = [6,2,4,3,7,5,3,2,4,1,8,3,3,4,5,8,9,4,5,3,2,5,4,6,8,2,2,4,4,3,5,1,3,1,2,6,9,8,6,7,5,6,3,4,6,5,5,7,7,4,2,3,8,9,7,8,3,3,4,5,8,7,6,9,8,7,6,8,3,3,4,5,7]
#big = [[2,3,3,4,5,8,5,7,6,3,3,4,5,8,9,3,3,4,5,2],[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']]
#small = [3,3,4,5,8]
#n = 6
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import time
import collections
import more_itertools



# Searches list to determine how many times small list is included in big list
def contains(small, big):
    counter = 0
    # initiating list of indexes. N.B. indexlist gives LAST index of sequence, not first
    coords = []
    for i in range(len(big[0])-len(small)+1):
        for j in range(len(small)):
            coord = []
            if big[0][i+j] != small[j]:
                break
        else:
            counter += 1
            for k in range(0,j+1):
                coord.append([big[1][i + k], big[2][i + k]])
            coords.append(coord)
    if counter > 0:
        return counter, coords
    return False

def findrepeats(sequence, n_letters):
    time_start = time.time()
    fulldict = {}
    # Iterating through all the short-sequences of n letters in the list
    for i in range(0, len(sequence[0]) - n_letters):
        shortliststr = ""
        shortlist = sequence[0][i:i + n_letters]
        for number in shortlist:
            shortliststr = shortliststr + "." + str(number)
        # If short-sequence is found in full sequence more than once (i.e. itself), add to dict
        if contains(shortlist, sequence)[0] > 1 and len(shortlist) == n_letters:
            fulldict[shortliststr] = contains(shortlist, sequence)
    time_elapsed = time.time() - time_start
    print(time_elapsed)
    return fulldict

def iterrepeats(sequence, n_letters):
    #time_start = time.time()
    fulldict = {}
    windows = [
        tuple(window)
        for window in more_itertools.windowed(sequence, n_letters)
    ]
    counter = collections.Counter(windows)
    for window, count in counter.items():
        if count > 1:
            fulldict[window] = count
    #time_elapsed = time.time() - time_start
    #print(time_elapsed)
    return fulldict

def findallrepeats(sequence, min_letters, max_letters):
    fulldict = {}
    sequence = list_convert(sequence)
    # Iterating through all possible n_letters in findrepeats() between given range
    for i in range(min_letters, max_letters):
        newdict = findrepeats(sequence, i)
        fulldict.update(newdict)
    return fulldict



def chakradown(chakra): 
    # Create an empty list 
    row_list =[]  
    # Iterate over each row 
    for i, rows in chakra.iterrows(): 
        # Create list for the current row ([value, row number, column number])
        for j, number in enumerate(rows):
            row_list.append([number, i, j])
        # append the list to the final list 
    return row_list
  
def chakraright(chakra):
    # Create an empty list 
    col_list = []  
    # Iterate over each row 
    for j, columns in chakra.iteritems(): 
        # Create list for the current row 
        for i, number in enumerate(columns):
            col_list.append([number, i, j])
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
    for i in range(1, width - 1):
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
    for i in range(1, width - 1):
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
            strings.append([letter, lettercoords[1], lettercoords[0]])
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
    dict3 = findallrepeats(ul, min_letters, max_letters)
    dict4 = findallrepeats(ur, min_letters, max_letters)
    return dict1, dict2, dict3, dict4

def onedirection(chakra, min_letters, max_letters):
    down = chakradown(chakra)
    right = chakraright(chakra)
    ul = diagonal_strings_up_left(chakra)
    ur = diagonal_strings_up_right(chakra)
    alldirections = down + right + ul + ur
    dict1 = findallrepeats(alldirections, min_letters, max_letters)
    return dict1

def list_convert(list_of_lists):
    newlist = [[],[],[]]
    for item in list_of_lists:
        newlist[0].append(item[0])
        newlist[1].append(item[1])
        newlist[2].append(item[2])
    return newlist

def create_colors(coord_list0,coord_list1,coord_list2,coord_list3,x):
    #copy df to new - original data are not changed
    df1 = x.copy()
    #select all values to default value - no color
    df1.loc[:,:] = 'w'
    #overwrite values with green and red color
    for coord in coord_list0:
        df1.loc[(coord[1],coord[0])] = 'y'
    for coord in coord_list1:
        df1.loc[(coord[1],coord[0])] = 'b'
    for coord in coord_list2:
        df1.loc[(coord[1],coord[0])] = 'g'
    for coord in coord_list3:
        df1.loc[(coord[1],coord[0])] = 'r'
    #return color df
    return df1    



def coord_list(dictionary):
    coordlist = []
    for item in dictionary.values():
        for coordset in item[1]:
            for coord in coordset:
                coordlist.append(coord)
    return coordlist

def create_colors_single(coord_list0,x):
    #copy df to new - original data are not changed
    df1 = x.copy()
    #select all values to default value - no color
    df1.loc[:,:] = 'w'
    #overwrite values with green and red color
    for coord in coord_list0:
        df1.loc[(coord[0],coord[1])] = 'y'
    #return color df
    return df1    

def singlecolour(chakras, min_letters, max_letters, file_name):
    chakra = pd.DataFrame(chakras)
    dict_all = onedirection(chakra, min_letters, max_letters)
    alist = coord_list(dict_all)
    colours = create_colors_single(alist, chakra)
            
    
    fig, ax = plt.subplots()
    
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    
    df = chakra
    
    the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellColours = colours.values)
    
    
    plt.savefig(str(file_name) + '.png', dpi = 250)
    plt.close()
    
    return

def multicolourprint(chakras, min_letters, max_letters, file_name):
    chakra = pd.DataFrame(chakras)
    dict1_down, dict1_right, dict1_ul, dict1_ur = alldirections(chakra, min_letters, max_letters)


    alist = coord_list(dict1_ul)
    blist = coord_list(dict1_ur)
    clist = coord_list(dict1_down)
    dlist = coord_list(dict1_right)
    
    
    
    
    colours = create_colors(alist, blist, clist, dlist, chakra)
            
    
    
    ###########################
    plt.ioff()
    fig, ax = plt.subplots()
    
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    
    df = chakra
    
    the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellColours = colours.values)
    
    
    plt.savefig(str(file_name) + '.png', dpi = 250)
    plt.close()
    
    ###########################
    return

dict_down, dict_right, dict_ul, dict_ur = alldirections(chakra3, 5, 14)


alist = coord_list(dict_ul)
blist = coord_list(dict_ur)
clist = coord_list(dict_down)
dlist = coord_list(dict_right)

alist = alist + blist + clist + dlist 



colours = create_colors(alist, blist, clist, dlist, chakra1)

dict_all = onedirection(chakra1, 6, 14)

def splitter(lst):
    jump = int(len(lst)/4)
    a = lst[0:jump]
    b = lst[jump:jump * 2]
    c = lst[jump * 2: jump * 3]
    d = lst[jump*3:]
    return a, b, c, d

alist = coord_list(dict_all_ed1)
colours = create_colors_single(alist, chakra1)

alist, blist, clist, dlist = splitter(alist)
colours = create_colors(alist, blist, clist, dlist, chakra1)        


###########################
fig, ax = plt.subplots()

# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

df = chakra1

the_table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellColours = colours.values)


plt.show()

###########################


multicolour(chakra1, 5, 12)
multicolour(chakra2, 5, 12)
multicolour(twochakra1, 5, 12)
multicolour(chakra8_11, 5, 12)




def ultradirection(chakra1, chakra2, chakra3, chakra4, min_letters, max_letters):
    down = chakradown(chakra1)
    right = chakraright(chakra1)
    ul = diagonal_strings_up_left(chakra1)
    ur = diagonal_strings_up_right(chakra1)
    alldirections = down + right + ul + ur
    down = chakradown(chakra2)
    right = chakraright(chakra2)
    ul = diagonal_strings_up_left(chakra2)
    ur = diagonal_strings_up_right(chakra2)
    alldirections += down + right + ul + ur
    down = chakradown(chakra3)
    right = chakraright(chakra3)
    ul = diagonal_strings_up_left(chakra3)
    ur = diagonal_strings_up_right(chakra3)
    alldirections += down + right + ul + ur
    down = chakradown(chakra4)
    right = chakraright(chakra4)
    ul = diagonal_strings_up_left(chakra4)
    ur = diagonal_strings_up_right(chakra4)
    alldirections += down + right + ul + ur
    dict1 = findallrepeats(alldirections, min_letters, max_letters)
    return dict1


dict_all_ed1 = {key:val for key, val in dict_all.items() if key.count('.') > 11}



import copy
alist = coord_list(dict_all)

dict_all_copy = copy.deepcopy(dict_all)
f  =  open("dict_all.txt", "w")
f.write( str(dict_all) )
f.close()

def even_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
chakras_all_8 = [chakras_1, chakras_2, chakras_3, chakras_4, chakras_5, chakras_6, chakras_7, chakras_8]

import time

start_time = time.time()
for i, chakrasdict in enumerate(chakras_all_8):
    print(str(i))
    elapsed_time = start_time - time.time()
    print('Time :')
    print(elapsed_time)
    for num, chak in chakrasdict.items():
        multicolourprint(chak, 6, 12, num)

for num, chak in chakras_2.items():
        multicolour(chak, 5, 12, num)
        
start_time = time.time()
for i, chakrasdict in enumerate(chakras_all_8):
    print(str(i))
    elapsed_time = start_time - time.time()
    print('Time :')
    print(elapsed_time)
    for num, chak in chakrasdict.items():
        singlecolour(chak, 6, 12, str(6) + str(num))
        
start_time = time.time()
for i, chakrasdict in enumerate(chakras_all_8):
    print(str(i))
    elapsed_time = start_time - time.time()
    print('Time :')
    print(elapsed_time)
    for num, chak in chakrasdict.items():
        singlecolour(chak, 5, 12, str(5) + str(num))
        
chakra = pd.DataFrame(chakras_1['1_1_2'])
down = chakradown(chakra)
right = chakraright(chakra)
ul = diagonal_strings_up_left(chakra)
ur = diagonal_strings_up_right(chakra)
alldirections = down + right + ul + ur
alldirections = list_convert(alldirections)



sequence = [
    2, 1, 4, 3, 12, 8, 3, 3, 4, 16, 2, 9, 9,
    8, 3, 3, 4, 1, 4, 3, 4, 8, 3, 3, 4,
]
size = 3
windows = [
    tuple(window)
    for window in more_itertools.windowed(sequence, size)
]
counter = collections.Counter(windows)
for window, count in counter.items():
    if count > 1:
        print(window, count)
        
        
###################

all_chakras = [chakras_1, chakras_2, chakras_3, chakras_4, chakras_5, chakras_6, chakras_7, chakras_8]

def list_from_all(all_chakras):
    full_list = []
    for chakras in all_chakras:
        for name, chakra in chakras.items():
            chakra = pd.DataFrame(chakra)
            down = chakradown(chakra)
            right = chakraright(chakra)
            ul = diagonal_strings_up_left(chakra)
            ur = diagonal_strings_up_right(chakra)
            alldirections = down + right + ul + ur
            full_list.extend(alldirections)
    return full_list
        
