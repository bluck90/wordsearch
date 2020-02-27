# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:49:47 2020

@author: btgl1e14
"""

import numpy as np
import copy


# Find all instances of a letter in the wordsearch and return the coordinates
def find_initial_coords(letter, matrix):
    initial_coords = [[line_index, char_index]
    for line_index, line in enumerate(matrix)
        for char_index, char in enumerate(line)
            if char == letter]
    return initial_coords


# Find all direct neighbours of a given coordinate which match a given character
def matched_neighbours(coord, letter, matrix, row_length, col_length):
    # Moving back one and down one so can easily implement for loop (I know not necessary, but was the way I saw it in my head, so kept it)
    coordx = coord[0] -1
    coordy = coord[1] -1
    neighbours = []
    for i in range(0,3):
        for j in range(0,3):
            coordxmatch = coordx + i
            coordymatch = coordy + j
            # Ensuring coordinate is not out of range
            if coordxmatch < 0 or coordymatch < 0:
                continue
            if coordxmatch > row_length -1 or coordymatch > col_length -1:
                continue
            # Stopping the function returning coord if coord matches letter
            if i == 1 and j == 1:
                continue
            if matrix[coordxmatch][coordymatch] == letter:
                coordsmatch = [(coordxmatch),(coordymatch)]
                neighbours.append(coordsmatch)
    return neighbours


# Returning all matched neighbours from list of coords
def all_neighbours(initial_coords, matrix, letter, row_length, col_length):
    neighbour_coords = []
    for i, initial_coord in enumerate(initial_coords):
        neighbours = matched_neighbours(initial_coords[i], letter, matrix, row_length, col_length)
        neighbour_coords.append(neighbours)
    return neighbour_coords


# #Giving a list of vectors to show which way the word moves through the wordsearch
def direction_vectors(initial_coords, matched_coords):
    # Creating deep copy so original matched coordinates won't be affected (unnecessary paranoia?)
    directions = copy.deepcopy(matched_coords)
    for i, initial_coord in enumerate(initial_coords):
        for j, direction in enumerate(directions[i]):
            directions[i][j] = np.subtract(directions[i][j], initial_coords[i])
    return directions


# Returns output of all the coordinates needed to spell out searchword
def find_all_coords(initial_coords, directions, matrix, row_length, col_length, searchword):
    all_coords = []
    for i, initial_coord in enumerate(initial_coords):
        tempcoord = []
        for j, direction in enumerate(directions[i]):
            all_coord = []
            tempcoord = np.add(initial_coords[i], directions[i][j])
            all_coord.append(np.array(initial_coords[i]))
            all_coord.append(tempcoord)
            tempcoord = np.add(tempcoord, directions[i][j])
            all_coord.append(tempcoord)
            if tempcoord[0] < 0 or tempcoord[0] > (row_length - 1) or tempcoord[1] < 0 or tempcoord[1] > (col_length - 1):
                continue
            if matrix[tempcoord[0]][tempcoord[1]] == searchword[2]:
                all_coords.append(all_coord)
    return all_coords


# Combining all functions
def win_wordsearch(searchword, wordsearch):
    matrix = wordsearch.split()
    row_length = len(matrix)
    col_length = len(matrix[0])
    initial_coords = find_initial_coords(searchword[0], matrix)
    neighbour_coords = all_neighbours(initial_coords, matrix, searchword[1], row_length, col_length)
    directions = direction_vectors(initial_coords, neighbour_coords)
    all_coords = find_all_coords(initial_coords, directions, matrix, row_length, col_length, searchword)
    return all_coords

wordsearch = 'doggo oogod gogdg oodgo dgood ododg ggodo'
searchword = 'dog'
results = win_wordsearch(searchword, wordsearch)














"""
Scrap below




# Return letter from coordinates
def coord_char(coord, matrix):
    return matrix[coord[0]][coord[1]]

def convert_to_word(coords, matrix):
    return ''.join([coord_char(coord, matrix)
            for coord in coords])

def test_words(results, matrix):
    word = ''
    words = []
    for result in results:
        word = convert_to_word(result, matrix)
        words.append(word)
    return words

words = test_words(results, wordsearch)
    
    searchword = 'god'
    initial_coords = find_initial_coords(searchword[0], matrix)
    neighbour_coords = all_neighbours(initial_coords, matrix)
    directions = direction_vectors(initial_coords, neighbour_coords)

searchwords = ['god','dog']





initial_coordsneighbours = []
for i, initial_coord in enumerate(initial_coords):
    neighbours = matched_neighbours(initial_coords[i], 'o', matrix, 3, 4)
    initial_coordsneighbours.append(neighbours)


all_coords = []
foundword = ''
foundwords = []
for i, initial_coord in enumerate(initial_coords):
    
    tempcoord = []
    for j, direction in enumerate(directions[i]):
        all_coord = []
        foundword = ''
        foundword = foundword + matrix[initial_coords[i][0]][initial_coords[i][1]]
        tempcoord = np.add(initial_coords[i], directions[i][j])
        all_coord.append(np.array(initial_coords[i]))
        all_coord.append(tempcoord)
        foundword = foundword + matrix[tempcoord[0]][tempcoord[1]]
        tempcoord = np.add(tempcoord, directions[i][j])
        all_coord.append(tempcoord)
        if tempcoord[0] < 0 or tempcoord[0] > 2 or tempcoord[1] < 0 or tempcoord[1] > 3:
            continue
        if matrix[tempcoord[0]][tempcoord[1]] == 'd':
            all_coords.append(all_coord)
            foundword = foundword + matrix[tempcoord[0]][tempcoord[1]]
            foundwords.append(foundword)
        
    
# all_coords gives coordinates











directions = []
direction = []
for i, initial_coordsneighbour in enumerate(initial_coordsneighbours):
    for j, coordstn in enumerate(initial_coordsneighbour):
        direction = np.subtract(initial_coordsneighbours[i][j], initial_coords[i])
        directions.append(direction)


    
     



neighbour = matched_neighbours(initial_coords[0],'g',matrix,3,4)


coordx = initial_coords[0][0] -1
coordy = initial_coords[0][1] -1
neighbours = []
for i in range(0,3):
    for j in range(0,3):
        coordxmatch = coordx + i
        coordymatch = coordy + j
        # Ensuring coordinate is not out of range
        if coordxmatch < 0 or coordymatch < 0:
            continue
        if coordxmatch > 3 -1 or coordymatch > 4 -1:
            continue
        # Stopping the function returning coord if coord matches char
        if i == 1 and j == 1:
            continue
        if matrix[coordxmatch][coordymatch] == 'g':
            coordsmatch = [(coordxmatch),(coordymatch)]
            neighbours.append(coordsmatch)


neighbours = []

for i in range(0,3):
    for j in range(0,3):
        coordx = 0
        coordy = 2
        coordxinit = coordx - 1
        coordyinit = coordy -1
        coordxmatch = coordxinit + i
        coordymatch = coordyinit + j     
              
        if coordxmatch < 0 or coordymatch < 0:
            continue
        if coordxmatch > 3 -1 or coordymatch > 4 -1:
            continue
        # Stopping the function returning coord if coord matches char
        if i == 1 and j == 1:
            continue
        if matrix[coordxmatch][coordymatch] == 'g':
            coordsmatch = [(coordxmatch),(coordymatch)]
            neighbours.append(coordsmatch)
            
"""

        
        
        
