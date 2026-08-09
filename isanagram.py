from collections import Counter

def is_anagram_pythonic_way(s: str, t: str) -> bool:
    """
    Determine whether two strings are anagrams using Counter.

    This method compares the character-frequency maps of both strings.
    If the maps are identical, the strings contain the same characters
    with the same counts and are therefore anagrams.

    Parameters
    ----------
    s : str
        The first string to compare.
    t : str
        The second string to compare.

    Returns
    -------
    bool
        True if the strings are anagrams, otherwise False.
    """
    return Counter(s) == Counter(t)


from collections import defaultdict

def isAnagram(s, t):
    """
    Determine whether two strings are anagrams using a character-frequency
    comparison.

    This function builds a frequency map of characters from the first string
    and then subtracts counts using the second string. If both strings contain
    exactly the same characters with the same frequencies, all counts return
    to zero and the strings are considered anagrams.

    Parameters
    ----------
    s : str
        The first string to compare.
    t : str
        The second string to compare.

    Returns
    -------
    int
        1 if the strings are anagrams, otherwise 0.
    """
    
    counter = defaultdict(int)

    if len(s) != len(t):
        return 0
    

    for ch in s:
        counter[ch] +=1

    for ch in t:
        if counter[ch] == 0:
            return 0
        counter[ch] -=1

    for val in counter.values():
        if val != 0:
            return 0
          
    return 1


def is_anagram_no_counter(s: str, t: str) -> bool:
    """
    Determine whether two strings are anagrams using a manual
    character-frequency dictionary.

    This method increments counts for characters in the first string
    and decrements them for the second. If all counts return to zero,
    the strings are anagrams.

    Parameters
    ----------
    s : str
        The first string to compare.
    t : str
        The second string to compare.

    Returns
    -------
    bool
        True if the strings are anagrams, otherwise False.
    """
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return all(count == 0 for count in freq.values())



def is_anagram_v2(s: str, t: str) ->bool:

    if len(s) != len(t):
        raise ValueError(f" Length S: {s} not equal Length T: {t}" )
    
    freq =  {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if freq.get(ch, 0) == 0:
            return False
        freq[ch] -= 1

    return True


import timeit

# Test input
STR1 = "listen"
STR2 = "silent"

# Number of iterations
ITER = 1_000_000

tests = {
    "pythonic way": "is_anagram_pythonic_way(STR1, STR2)",
    "default dic way": "isAnagram(STR1, STR2)",
    "no counter way": "is_anagram_no_counter(STR1, STR2)",
    "clean version": "is_anagram_v2(STR1, STR2)",
}

setup = """
from __main__ import (
    is_anagram_pythonic_way,
    isAnagram,
    is_anagram_no_counter,
    is_anagram_v2,
    STR1,
    STR2
)
"""

print(f"Benchmarking with STRING ONE={STR1} and STRING TWO={STR2} for {ITER:,} iterations:\n")

# Print header
print(f"{'Method':20s} | {'Result':6s} | Time (seconds)")
print("-" * 50)

for name, stmt in tests.items():
    # Compute True/False once (not inside timeit)
    result = eval(stmt)

    # Benchmark timing
    t = timeit.timeit(stmt, setup=setup, number=ITER)

    # Print row
    print(f"{name:20s} | {str(result):6s} | {t:.6f}")