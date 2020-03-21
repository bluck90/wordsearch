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

wordsearch = wordsearch_rand(45,45)

# To return wordsearches with higher likelihood of English words
def rand_weighted(n):
    alphabet = "etaoinshrdlcumwfgypbvkjxqz"
    alphabet_letters = [] 
    alphabet_letters[:0] = alphabet 
    choice = random.choices(alphabet_letters, weights = [0.12702, 0.09056, 0.08167, 0.07507, 0.06966, 0.06749, 0.06327, 0.06094, 0.05987, 0.04253, 0.04025, 0.02782, 0.02758, 0.02406, 0.0236, 0.02228, 0.02015, 0.01974, 0.01929, 0.01492, 0.00978, 0.00772, 0.00153, 0.0015, 0.00095, 0.00074], k = n)
    choicelist = ''.join(choice)
    return choicelist

def wordsearch_rand_weighted(height, width):
    wordsearch = ''
    for i in range(1, height + 1):
        line = rand_weighted(width)
        wordsearch = wordsearch + line + ' '
    # slice removes the last space
    return wordsearch[:-1]

wordsearch = wordsearch_rand_weighted(45,45)
        