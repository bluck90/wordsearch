# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:10:18 2020

@author: btgl1e14
"""

_end = '*'

# takes in a list of words
def make_trie(*words):
    # creates our root dict()
    trie = dict()

    for word in words:
        # create a temporary dict based off our root
        # dict object
        temp_dict = trie

        for letter in word:
            # update our temporary dict and add our current
            # letter and a sub-dictionary
            temp_dict = temp_dict.setdefault(letter, {})

        # If our word is finished, add {'*': '*'}
        # this tells us our word is finished
        temp_dict[_end] = _end
    return trie

# Test our trie creation
trie = make_trie('hi', 'hello', 'howdy')
# print out our new trie
print(trie)