# Greeting a user
# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

# Example 1Copy Code
# What is your name? Sue
# Hello Sue.


# Example 2Copy Code
# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

name = input('What is your name? ')

# if name[-1] == '!':
#     print(f"HELLO {name}! WHY ARE WE YELLING?")
# else:
#     print(f"Hello {name}")

if name.endswith("!"):
    print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
else:
    print(f"Helo {name}.")
