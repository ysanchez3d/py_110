# Searching 101
# Write a program that solicits six (6) numbers from the user and prints a message that describes whether the sixth number appears among the first five.

numbers = []

numbers.append(input("Enter the 1st number: "))
numbers.append(input("Enter the 2nd number: "))
numbers.append(input("Enter the 3rd number: "))
numbers.append(input("Enter the 4th number: "))
numbers.append(input("Enter the 5th number: "))
last_number = input("Enter the last number: ")

numbers_list = ','.join(numbers)

if last_number in numbers:
    print(f"{last_number} is in {numbers_list}.")
else:
    print(f"{last_number} isn't in {numbers_list}.")

# Example 1
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 17
# 17 is in 25,15,20,17,23.

# Example 2
# Enter the 1st number: 25
# Enter the 2nd number: 15
# Enter the 3rd number: 20
# Enter the 4th number: 17
# Enter the 5th number: 23
# Enter the last number: 18

# 18 isn't in 25,15,20,17,23.
# Show