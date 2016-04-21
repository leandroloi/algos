# -*- coding: utf-8 -*-
import sys

__author__ = 'leandroloi'
__credits__ = ["Leandro Loi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Leandro Loi"
__email__ = "leandroloi at gmail dot com"
__status__ = "Development"

from math import log
import string


# remove any spaces or special characters
def normalize_string(s):
    table = string.maketrans("", "")
    s = s.lower()
    s = s.replace(' ', '')
    s = s.replace('’', '')
    #print s
    s = s.translate(table, string.punctuation)

    return s


# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open("dict.txt").read().split()  # Dictionary sorted by word frequency importance
wordcost = dict(
    (k, log((i + 1) * log(len(words)))) for i, k in enumerate(words))  # calculates the frequency for each word

# adding numbers to words with a cost(frequency) of log(2)
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for n in nums:
    wordcost[n] = log(2)

maxword = max(len(x) for x in words)


def infer_spaces(s):
    s = normalize_string(s)

    """Uses dynamic programming to infer the location of spaces in a string
    without spaces."""

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i - maxword):i]))
        return min((c + wordcost.get(s[i - k - 1:i], 9e999), k + 1) for k, c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1, len(s) + 1):
        c, k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i > 0:
        c, k = best_match(i)
        assert c == cost[i]
        out.append(s[i - k:i])
        i -= k

    return " ".join(reversed(out))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        for line in open(sys.argv[1]).readlines():
            print infer_spaces(line)
    else:
        print "Usage: python inferspaces.py <text file>"

