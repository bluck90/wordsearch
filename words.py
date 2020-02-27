# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 19:11:55 2020

@author: btgl1e14
"""

from nltk import everygrams
import enchant
word = 'godaddy'
[''.join(_ngram) for _ngram in everygrams(word) if d.check(''.join(_ngram))]
d = enchant.Dict("en_US")
# Exclude single char words.
[''.join(_ngram) for _ngram in everygrams(word) if d.check(''.join(_ngram)) and len(_ngram) > 1]

from nltk import corpus





import nltk.corpus.reader.wordlist as words

english_vocab = set(w.lower() for w in words())

english_vocab = set(w.lower() for w in nltk.corpus.words.words())


import nltk
nltk.download()

st = "doggooogodgogdgoodgodgoodododgggodo"

all_words = {st[i:j + i] for j in range(3, len(st)) for i in range(len(st)- j + 2)}

english_vocab = set(w.lower() for w in corpus.words())

english_vocab.intersection(all_words)

matrix = wordsearch.split()

my_set = {1, 2, 3}
print(my_set)

for line in matrix:
    for letter in line:
        