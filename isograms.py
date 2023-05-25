"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false
"""


def is_isogram(string):
    is_not = []
    convert = string.lower()
    for s in convert:
        if convert.count(s) > 1:
            is_not.append(s)
        else:
            pass;
    return True if len(is_not) == 0 else False


