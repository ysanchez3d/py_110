# Write a function that returns the next to last word in the string argument.

# Words are any sequence of non-blank characters.

# You may assume that the input string will always contain at least two words.

def penultimate(str):
    words = str.split()
    return words[-2]


# Examples
# # These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
