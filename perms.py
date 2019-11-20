def process(stem, alphabet):
    """Produces (as tuples) all permutations of a set of symbols
       from an alphabet stem should be supplied as an empty list"""
    if not alphabet: #all symbols already in stem
        yield tuple(stem)
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
from itertools import permutations
from timeit import timeit

def test_empty():
    assert {tuple(x) for x in process([], [])} =={()}

def test_one_element():
    assert {tuple(x) for x in process([], {1})} == {(1, )}

def test_two_elements():
    assert {x for x in process([], {1, 2})} == {(1, 2), (2, 1)}

def test_three_elements():
    assert {x for x in process([], {1, 2, 3})} == {(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)}

def test_nine_elements():
    assert {tuple(x) for x in process([], set(range(9)))} == {x for x in permutations(range(9))}

if __name__ == '__main__':
    t1 = timeit("{tuple(x) for x in process([], set(range(7)))}", "from __main__ import process", number=100)
    t2 = timeit("{x for x in permutations(range(7))}", "from __main__ import process, permutations", number=100)

    print(f"process: {t1:.5f} permutations: {t2:.5f} faster by: {t1/t2:.1f} times")
