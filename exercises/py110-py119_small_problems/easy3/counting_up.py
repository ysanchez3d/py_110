# Counting Up
# Write a function that takes an integer argument and returns a list containing all integers between 1 and the argument (inclusive), in ascending order.

# You may assume that the argument will always be a positive integer.

def sequence(n):
    return [num for num in range(1, n + 1)]




# Examples
print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True
