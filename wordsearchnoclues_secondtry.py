# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:43:22 2020

@author: btgl1e14
"""

import numpy as np

st = ["doggo", "oogod", "godgo"]
wordsearchraw = 'doggo oogod gogdg oodgo dgood ododg ggodo'
wordsearchsplit = wordsearchraw.split(" ")

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

strings_set = wordsearch_strings_set(wordsearchsplit)

import nltk

english_vocab = set(w.lower() for w in nltk.corpus.words.words())

words = english_vocab.intersection(strings_set)