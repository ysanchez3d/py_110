# Practice Problem 1
# For each object shown below, demonstrate how you would access the letter g.


lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
# print(f"1: {lst1[2][1][3]}")

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]
# print(f"2: {lst2[1]['third'][0]}")

lst3 = [['abc'], ['def'], {'third': ['ghi']}]
# print(f"3: {lst3[2]['third'][0][0]}")

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
# print(f"4: {dict1['b'][1]}")

# # This one is much more challenging than it looks! Try it, but don't
# # stress about it. If you don't solve it in 10 minutes, you can look
# # at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}

# print(f"5: {tuple(dict2['3rd'])[0]}")


# Practice Problem 2
# For each of these collection objects, demonstrate how you would change the value 3 to 4.

lst1 = [1, [2, 3], 4]
lst1[1][1] = 4
# print(lst1)

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
lst2[2] = 4
# print(lst2)

dict1 = {'first': [1, 2, [3]]}

dict1['first'][2] = 4
# print(dict1)

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}

dict2['a']['a'][2] = 4
# print(dict2)


# Practice Problem 3
# Given the following code, what will the final values of a and b be? Try to answer without running the code.

a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

# a = 2
# b = [3, 8]


# Practice Problem 4
# One of the most frequently used real-world string operations is that of "string substitution," where we take a hard-coded string and modify it with various parameters from our program.

# Given the object shown below, print the name, age, and gender of each family member:


munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}
# Each output line should follow this pattern:


# (name) is a (age)-year-old (male or female).
for name, stats in munsters.items():
    print(f"{name} is a {stats['age']}-year-old {stats['gender']}."
)


# Expected Output
# Herman is a 32-year-old male.
# Lily is a 30-year-old female.
# Grandpa is a 402-year-old male.
# Eddie is a 10-year-old male.
# Marilyn is a 23-year-old female.

