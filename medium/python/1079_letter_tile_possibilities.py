'''
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make
using the letters printed on those tiles.

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
"ABA", "BAA".

https://leetcode.com/problems/letter-tile-possibilities/description/
'''

import itertools


class Solution(object):
    def numTilePossibilities(tiles):
        list = []
        sequences = []
        for letter in tiles:
            list.append(letter)
        for item in range(len(list)+1):
            for sequence in itertools.permutations(list, item):
                sequences.append(sequence)
        return (len(set(sequences)) - 1)
    print(numTilePossibilities("AAB"))
