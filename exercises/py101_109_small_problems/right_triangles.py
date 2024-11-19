# Right Triangles
# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.


def triangle(size):
    level = 1

    while level <= size:
        spaces = (size - level) * " "
        delimeters = level * "*"
        print(spaces + delimeters)
        level += 1



# Example 1
triangle(5)
# Output for Example 1Copy Code
#     *
#    **
#   ***
#  ****
# *****


# Example 2
triangle(9)
# Output for Example 2Copy Code
#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********
