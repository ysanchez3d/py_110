# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.

# Example 1Copy Code
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.
# Example 2Copy Code
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.


num = int(input("Please enter an integer greater than 0: "))
operation = input('Enter "s" to compute the sum, or "p" to compute the product. : ')

if operation == "s":
    sum = 0
    for num in range(1, num + 1):
        sum += num

    print(f"The sum of the integers between 1 and {num} is {sum}")
else:
    product = 1
    for num in range(1, num + 1):
        product *= num

    print(f"The product of the integers between 1 and {num} is {product}.")