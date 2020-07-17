# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:24:33 2020

@author: btgl1e14
"""
import numpy as np


def spiral_coords(wordsearch, initial_coord, chirality, vector_offset = 0):    
    """chirality takes inputs 1 or 2 for clockwise and counterclockwise respectively.
    vector_offset defines the direction in which the spiral starts, if 0 the spiral starts downwards."""    
    if chirality == 1:
        vectors = [[0,1],[1,0],[0,-1],[-1,0]]
    elif chirality == 2:
        vectors = [[0,-1],[1,0],[0,1],[-1,0]]
    else:
        return "Chirality value must be either 1 (CW) or 2 (CCW)"
    initial_coord = np.add(initial_coord,[0,0]) # Just ensuring it is a numpy vector
    current_coord = initial_coord
    coord_list = []
    coord_list.append(initial_coord)
    for i in range(1, 2*len(wordsearch) + 1):        
        arm_length = int((i + 1) / 2)
        vector_index = (i + vector_offset) % 4
        for j in range(1, arm_length + 1):
            current_coord = np.add(current_coord, vectors[vector_index])
            if current_coord[0] >= 0 and current_coord[0] < len(wordsearch) and current_coord[1] >= 0 and current_coord[1] < len(wordsearch[0]):
                coord_list.append(current_coord)
            else:
                return coord_list

# Getting list of strings from coords
def strings_from_spiral_coords(wordsearch, coords):
    strings = []
    for lettercoords in coords:
        letter = wordsearch[lettercoords[0]][lettercoords[1]]
        strings.append([letter, lettercoords[0], lettercoords[1]])
    return strings

spiralone = strings_from_spiral_coords(chakras_1['1_1_1'],spiral_coords(chakras_1['1_1_1'],[12,13],2, vector_offset = 1))
wordsearch = chakras_1['1_1_1']
spiralcoords = spiral_coords(wordsearch,[13,13],1)
spiralone = strings_from_spiral_coords(wordsearch,spiralcoords)

def all_spiral_list(wordsearch, chirality, vector_offset = 0):
    full_list = []
    for i in range(0, len(wordsearch)):
        for j in range(0, len(wordsearch[0])):
            coords = spiral_coords(wordsearch, [i, j], chirality, vector_offset)
            stringlist = strings_from_spiral_coords(wordsearch, coords)
            full_list.append(stringlist)
    return full_list
            
        


    
        

    
        
    