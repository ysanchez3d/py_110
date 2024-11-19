# Bannerizer
# Write a function that takes a short line of text and prints it within a box.

def print_in_box(text):
    horizontal_rule = f'+-{"-" * len(message)}-+'
    empty_line = f'| {" " * len(message)} |'

    print(horizontal_rule)
    print(empty_line)
    print(f'| {message} |')
    print(empty_line)
    print(horizontal_rule)


# Example 1
# print_in_box('To boldly go where no one has gone before.')
# Output for Example 1
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+
# Example 2
# print_in_box('')
# Output for Example 2Copy Code
# +--+
# |  |
# |  |
# |  |
# +--+
# You may assume the output will always fit in your terminal window.

