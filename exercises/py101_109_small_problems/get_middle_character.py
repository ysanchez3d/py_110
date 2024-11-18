# Get Middle Character
# Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.

import math

def center_of(str):
    str_length = len(str)
    str_is_odd = str_length % 2 == 1
    str_mid = math.floor(str_length / 2)

    if str_is_odd:
        return str[str_mid]
    else:
        str_mid -= 1
        return str[str_mid:str_mid + 2]


# Examples
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
