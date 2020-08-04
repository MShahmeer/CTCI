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

Problem 4:
>>> palindrome_permutations("Tact Coa")
True
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


"""
Problem 3 - URLify:
Write a method to replace all spaces in a string with '%20: You may assume that
the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.
"""


def urlify(s: list, true_length: int) -> None:
    offset = len(s) - true_length
    for i in range(true_length - 1, -1, -1):
        if s[i] != ' ':
            s[i + offset] = s[i]
        else:
            s[i + offset - 2] = '%'
            s[i + offset - 1] = '2'
            s[i + offset] = '0'
            offset = offset - 2
# Time complexity: O(n), space complexity: O(1)


"""
Problem 4 - Palindrome Permutation:
Given a string, write a function to check if it is a permutation of a
palindrome. A palindrome is a word or phrase that is the same forwards and
backwards. A permutation is a rearrangement of letters.The palindrome does not
need to be limited to just dictionary words.
"""


def palindrome_permutations(s: str) -> bool:
    s = s.lower()
    s.replace(" ", "")
    letter_set = set(s)
    has_even_no = False
    if len(s) % 2 == 0:
        has_even_no = True
    for char in letter_set:
        odds = 0
        if s.count(char) % 2 != 0:
            odds += 1
            if has_even_no or (not has_even_no and odds > 1):
                return False
        if not has_even_no and odds == 0:
            return False
        return True
# Time complexity: O(n), space complexity: O(n)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
