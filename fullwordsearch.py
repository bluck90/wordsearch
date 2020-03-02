# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:43:22 2020

@author: btgl1e14
"""

import numpy as np
import nltk
import copy

wordsearch = 'doggo oogod gogdg oodgo dgood ododg ggodo'

# PART 1 - Find all English words in wordsearch

# returns list of strings upwards
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

# reverse strings
def reverse_strings(strings):
    reverse = [strings[i][::-1] for i in range(0, len(strings))]
    return reverse

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
        string = ''
        for lettercoords in stringcoords:
            letter = wordsearch[lettercoords[0]][lettercoords[1]]
            string = string + letter
        strings.append(string)
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

# combining all into set
def wordsearch_strings_set(wordsearch):
    forwards = wordsearch
    backwards =  reverse_strings(forwards)
    upwards = upwards_strings(wordsearch)     
    downwards = reverse_strings(upwards)
    upright = diagonal_strings_up_right(wordsearch)   
    downleft = reverse_strings(upright)
    upleft = diagonal_strings_up_left(wordsearch)
    downright = reverse_strings(upleft)    
    strings = forwards + backwards + upwards + downwards + upright + downleft + upleft + downright   
    strings_set = {strings[h][i:j+i] for h in range(0, len(strings)) for j in range(3,len(strings[h])+1) for i in range(0, (len(strings[h])+1)-j)}
    return strings_set

# Find real words in the string set
def realsolutions(wordsearch):
    # Getting wordsearch (from list of strings divided by space) into usable array
    wordsearchmatrix = wordsearch.split(" ")
    strings_set = wordsearch_strings_set(wordsearchmatrix)
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    solutions = english_vocab.intersection(strings_set)
    return solutions

# PART 2 - Return coordinates to all words in wordsearch

# Find all instances of a letter in the wordsearch and return the coordinates
def find_initial_coords(letter, matrix):
    initial_coords = [[line_index, char_index]
    for line_index, line in enumerate(matrix)
        for char_index, char in enumerate(line)
            if char == letter]
    return initial_coords

# Find all direct neighbours of a given coordinate which match a given character
def match_neighbours(coord, letter, matrix, row_length, col_length):
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
        neighbours = match_neighbours(initial_coords[i], letter, matrix, row_length, col_length)
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
    # Cycles through all coords given
    for i, initial_coord in enumerate(initial_coords):
        tempcoord = []
        # Cycles through all directions given for each coord
        for j, direction in enumerate(directions[i]):
            all_coord = []
            # Adding initial coord to list of coords
            all_coord.append(np.array(initial_coords[i]))
            tempcoord = initial_coords[i]
            # Adding direction vector to initial coord to get next coords
            for k, letter in enumerate(searchword):
                tempcoord = np.add(tempcoord, directions[i][j])
                if tempcoord[0] < 0 or tempcoord[0] > (row_length - 1) or tempcoord[1] < 0 or tempcoord[1] > (col_length - 1) or (k + 2) > len(searchword):
                    continue
                elif matrix[tempcoord[0]][tempcoord[1]] == searchword[k + 1]:
                    all_coord.append(tempcoord)
                    # Checking it has found the full word
                    if len(all_coord) == len(searchword):
                        # Adding list of coords to array of coords
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

# For multiple searchwords, returns a dict
def win_wordsearch_multi(searchwords, wordsearch):
    dictionary = {}
    for word in searchwords:
        results = win_wordsearch(word, wordsearch)
        dictionary[word] = results
    return dictionary

# PART 3 - The End
def solve_wordsearch(wordsearch):
    solutions = realsolutions(wordsearch)
    solved = win_wordsearch_multi(solutions, wordsearch)
    return solved

answers = solve_wordsearch(wordsearch)