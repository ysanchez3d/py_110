# Merge Sets
# Given two lists, convert them to sets and return a new set which is the union of both sets.

# Example
list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]

def merge_sets(list1, list2):
    return set(list1).union(set(list2))

print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13})
# Prints True