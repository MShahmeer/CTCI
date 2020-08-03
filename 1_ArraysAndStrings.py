"""
DOCTESTS:

Problem 1:
>>> is_unique("test")
False
>>> is_unique("abcdef")
True
>>> is_unique("")
True

Problem 2:
>>> check_permutations("racecar", "carecar")
True
>>> check_permutations("racecar", "not a racecar")
False
"""


"""
Problem 1 - Is Unique:
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique(s: str) -> bool:
    comp = set()
    for char in s:
        if char in comp:
            return False
        else:
            comp.add(char)
    return True
# Time complexity: O(n), space complexity: O(1)


"""
Problem 2 - Check Permutations:
Given two strings, write a method to decide if one's a permutation of the other.
"""


def check_permutations(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    comp1 = {}
    comp2 = {}
    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        if c1 in comp1:
            comp1[c1] = comp1[c1] + 1
        else:
            comp1[c1] = 0
        if c2 in comp2:
            comp2[c2] = comp2[c2] + 1
        else:
            comp2[c2] = 0
    return comp1 == comp2
# Time complexity: O(n), space complexity: O(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
