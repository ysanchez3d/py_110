# Double Char (Part 1)
# Write a function that takes a string, doubles every character in the string, then returns the result as a new string.

def repeater(s):
    repeat = ""

    for char in s:
        repeat += char * 2

    return repeat

# Examples
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True
