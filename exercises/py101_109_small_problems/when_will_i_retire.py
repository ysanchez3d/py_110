# When Will I Retire?
# Build a program that displays when the user will retire and how many years she has to work till retirement.

YEAR = 2024
age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))
RETIREMENT_YEAR = YEAR + (retirement_age - age)

print(f"It's {YEAR}. You will retire in {RETIREMENT_YEAR}.")
print(f"You have only {retirement_age - age} years of work to go!")

# Example
# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!
