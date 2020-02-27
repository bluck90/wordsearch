# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 16:49:47 2020

@author: btgl1e14
"""

import numpy as np
import copy

# Turns a string into a list
def matrixify(grid, separator='/n'):
    return grid.split(separator)


grid = 'dogg oogo gogd'
matrix = matrixify(grid, ' ')

# Return letter from coordinates
def coord_char(coord, matrix):
    return matrix[coord[0]][coord[1]]

def convert_to_word(coords, matrix):
    return ''.join([coord_char(coord, matrix)
            for coord in coords])
    


# Find all instances of a letter in the wordsearch and return the coordinates
def find_base_match(letter, matrix):
    base_matches = [[line_index, char_index]
    for line_index, line in enumerate(matrix)
        for char_index, char in enumerate(line)
            if char == letter]
    return base_matches


# Find all direct neighbours of a given coordinate which match a given character
def matched_neighbours(coord, char, matrix, row_length, col_length):
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
            # Stopping the function returning coord if coord matches char
            if i == 1 and j == 1:
                continue
            if matrix[coordxmatch][coordymatch] == char:
                coordsmatch = [(coordxmatch),(coordymatch)]
                neighbours.append(coordsmatch)
    return neighbours

# #Giving a list of vectors to show which way the word moves through the wordsearch
def direction_vectors(initial_coords, matched_coords):
    # Creating deep copy so original matched coordinates won't be affected
    directions = copy.deepcopy(matched_coords)
    for i, initial_coord in enumerate(initial_coords):
        for j, direction in enumerate(directions[i]):
            directions[i][j] = np.subtract(directions[i][j], coordstest[i])
    return directions

directions = direction_vectors(coordstest, coordstestneighbours)

searchwords = ['god','dog']
coordstest = find_base_match('g', matrix)

coordstestneighbours = []
for i, coordtest in enumerate(coordstest):
    neighbours = matched_neighbours(coordstest[i], 'o', matrix, 3, 4)
    coordstestneighbours.append(neighbours)


endcoords = []
foundword = matrix[coordstest[i][0]][coordstest[i][1]]
for i, coordtest in enumerate(coordstest):
    tempcoord = []
    for j, direction in enumerate(directions[i]):
        endcoord = []
        foundword = foundword + matrix[coordstest[i][0]][coordstest[i][1]]
        tempcoord = np.add(coordstest[i], directions[i][j])
        endcoord.append(coordstest[i])
        endcoord.append(tempcoord)
        foundword = foundword + matrix[tempcoord[0]][tempcoord[1]]
        tempcoord = np.add(tempcoord, directions[i][j])
        endcoord.append(tempcoord)
        if tempcoord[0] < 0 or tempcoord[0] > 2 or tempcoord[1] < 0 or tempcoord[1] > 3:
            continue
        if matrix[tempcoord[0]][tempcoord[1]] == 'd':
            endcoords.append(endcoord)
            foundword = foundword + matrix[tempcoord[0]][tempcoord[1]]
        foundword = foundword + " "
    
""" endcoords gives coordinates"""








"""


directions = []
direction = []
for i, coordstestneighbour in enumerate(coordstestneighbours):
    for j, coordstn in enumerate(coordstestneighbour):
        direction = np.subtract(coordstestneighbours[i][j], coordstest[i])
        directions.append(direction)


    
     



neighbour = matched_neighbours(coordstest[0],'g',matrix,3,4)


coordx = coordstest[0][0] -1
coordy = coordstest[0][1] -1
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

        
        
        
