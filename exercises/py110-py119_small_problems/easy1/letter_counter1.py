# Letter Counter (Part 1)
# Write a function that takes a string consisting of zero or more space-separated words and returns a dictionary that shows the number of words of different sizes.


def word_sizes(string):
    words = string.split()
    word_size_dict = {}

    for word in words:
        length = len(word)
        word_size_dict.setdefault(length, 0)
        word_size_dict[length] += 1

    return word_size_dict


# Words consist of any sequence of non-space characters.

# Examples
# # All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})
