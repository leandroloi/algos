# -*- coding: utf-8 -*-
__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

from itertools import permutations


def unscrambleWord(right_words, word):
    result = []
    chars = list(word)
    for c in permutations(chars, len(word)):
        unscrable = ''.join(c)
        if unscrable in right_words:
            result.append(unscrable)

    return result


if __name__ == '__main__':
    textbook = ['rike', 'erik', 'michael','leandro','ordnael']
    print unscrambleWord(textbook, 'erik') # Result => [‘Erik’, ‘Rike’]
