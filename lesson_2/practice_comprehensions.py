# Practice Problem 1
# Consider the following nested dictionary:


munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# Compute and display the total age of the family's male members. Try working out the answer two ways: first with an ordinary loop, then with a comprehension.

# The result should be 444.
loop_result = 0
for name, info in munsters.items():
    if info['gender'] == 'male':
        loop_result += info['age'] 

# print(loop_result)

all_ages = [info['age'] for name, info in munsters.items()
                if info['gender'] == 'male']

# print(sum(all_ages))


# Practice Problem 2
# Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order. Use a comprehension if you can. (Try using a for loop first.)

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# Expected result
# [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]

# The string values should be sorted as strings, while the numeric values should be sorted as numbers.

new_lst = []
# for inner_lst in lst:
#     new_lst.append(sorted(inner_lst))

# print(new_lst)

new_lst = [sorted(inner_lst) for inner_lst in lst]
# print(new_lst)


# Practice Problem 3
# Given the following data structure, return a new list with the same structure, but with the values in each sublist ordered in ascending order as strings (that is, the numbers should be treated as strings). Use a comprehension if you can. (Try using a for loop first.)


lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
# Expected result
# [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']]

new_lst = [sorted(sublist, key=str) for sublist in lst]
# print(new_lst)


# Practice Problem 4
# Given the following data structure, write some code that defines a dictionary where the key is the first item in each sublist, and the value is the second.


lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]
# Expected result
# Pretty printed for clarity
{
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
}

p4_result = {sublist[0]: sublist[1] for sublist in lst}
# print(p4_result)


# Practice Problem 5
# Given the following data structure, sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.

# Copy Code
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
# Note that the first sublist has the odd numbers 1 and 7; the second sublist has odd numbers 1, 5, and 3; and the third sublist has 1 and 3. Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list should look like this:

# Expected result
# [[1, 8, 3], [1, 6, 7], [1, 5, 3]]
# Try to use a comprehension in your solution.

def sum_odds(lst):
    odds = [num for num in lst if num % 2 == 1]
    return sum(odds)

p5_result = sorted(lst, key=sum_odds)
# print(p5_result)


# Practice Problem 6
# Given the following data structure, return a new list identical in structure to the original but, with each number incremented by 1. Do not modify the original data structure. Use a comprehension.

# Copy Code
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
# Expected result
# [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

p6_result = [{key: value + 1} for subitem in lst
                              for key, value in subitem.items()]
print(p6_result)





