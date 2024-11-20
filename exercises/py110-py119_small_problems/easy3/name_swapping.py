# Name Swapping
# Write a function that takes a string argument consisting of a first name, a space, and a last name. The function should return a new string consisting of the last name, a comma, a space, and the first name.

def swap_name(name):
    names = name.split()
    return names[1] + ", " + names[0]


# Example
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True
# You may assume that the names don't include middle names, initials, or suffixes ("Jr.", "Sr.").

