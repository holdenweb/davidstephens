def process(stem, alphabet):
    """outputs (as lists) all permutations of a set of symbols in alphabet
        stem should be supplied as an empty list"""
    if not alphabet: #all symbols already in stem
        yield stem
    else:
        acopy = set(alphabet) # local copy
        while acopy:
            s = acopy.pop()
            remaining = alphabet.difference(set([s]))
            xstem = list(stem)
            xstem.append(s)
            yield from process(xstem, remaining)

# Original code commented out
#stem = []
#alphabet = set([1, 2, 3, 4, 5])
#for combo in process(stem, alphabet):
    #print(combo)

#
# Additional testing added to ensure that changes don't affect the result
#
import pytest
from itertools import permutations

def test_empty():
    assert [x for x in process([], [])] == [[]]

def test_one_element():
    assert [x for x in process([], {1})] == [[1]]

def test_two_elements():
    assert [x for x in process([], {1, 2})] == [[1, 2], [2, 1]]

def test_three_elements():
    assert [x for x in process([], {1, 2, 3})] == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

def test_ten_elements():
    assert set([tuple(x) for x in process([], set(range(8)))]) == set((x for x in permutations(range(8))))
