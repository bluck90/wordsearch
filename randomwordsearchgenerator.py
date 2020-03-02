# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 16:29:45 2020

@author: btgl1e14
"""

import random
import string

def rand(n):
  alphabet = string.ascii_lowercase
  return ''.join(random.choice(alphabet) for i in range(n))

def wordsearch_rand(height, width):
    wordsearch = ''
    for i in range(1, height + 1):
        line = rand(width)
        wordsearch = wordsearch + line + ' '
    # slice removes the last space
    return wordsearch[:-1]

wordsearch = wordsearch_rand(66,66)
        
        