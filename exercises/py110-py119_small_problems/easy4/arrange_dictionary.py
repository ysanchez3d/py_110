
# Give us your feedback
# Arrange a Dictionary
# Given a dictionary, return its keys sorted by the values associated with each key.

def get_value(tup):
    return tup[1]

def order_by_value(dictionary):
    srted = sorted(dictionary.items(), key=get_value)
    return [item[0] for item in srted]


# Example
my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True