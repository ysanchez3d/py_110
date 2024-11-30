# Immutable Intersection
# Transform two lists into frozen sets and find their common elements.

def intersection(list1, list2):
    return frozenset(set(list1).intersection(set(list2)))



list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True
