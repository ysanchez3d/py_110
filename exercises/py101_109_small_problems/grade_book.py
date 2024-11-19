# Grade Book
# Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.


def get_grade(grade1, grade2, grade3):
    average = (grade1 + grade2 + grade3) / 3

    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'
# Tested values are all between 0 and 100. There is no need to check for negative values or values greater than 100.

# Examples
print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
