# Sequence Count
# Create a function that takes two integers as arguments. The first argument is a count, and the second is the starting number of a sequence that your function will create. The function should return a list containing the same number of elements as the count argument. The value of each element should be a multiple of the starting number.

# You may assume that count will always be an integer greater than or equal to 0. The starting number can be any integer. If the count is 0, the function should return an empty list.

def sequence(count, start):
    result = []

    n = 1
    while len(result) < count:
        result.append(start * n)

        n += 1

    return result

# Examples
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True
