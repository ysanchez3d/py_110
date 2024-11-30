# Unique Elements
# From two list arguments, determine the elements that are unique to the first list. The return value should be a set.

def unique_from_first(list1, list2):
    return set(list1).difference(set(list2))


# Example
list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})
