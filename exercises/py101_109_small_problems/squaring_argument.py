# Squaring an Argument
# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).


from multiply_two_numbers import multiply

def square(num):
    return multiply(num, num)





# Examples
print(square(5) == 25)   # True
print(square(-8) == 64)  # True
