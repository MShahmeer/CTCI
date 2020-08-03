"""
Problem 1 - Is Unique:
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

>>> is_unique("test")
False
>>> is_unique("abcdef")
True
>>> is_unique("")
True
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


if __name__ == "__main__":
    import doctest
    doctest.testmod()
