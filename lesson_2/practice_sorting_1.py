# Practice Problem 1
# Sort the following list of numbers first in ascending numeric order, then in descending numeric order. Do not mutate the list.


lst = [10, 9, -6, 11, 7, -16, 50, 8]

# print(sorted(lst))
# print(sorted(lst, reverse=True))
# Expected result
# [-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
# [50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort

# 2
# Mutating the list
# lst.sort()
# lst.sort(reverse=True)
# print(lst)


# Sort list as strings
def to_str(x):
    return str(x)

# lst.sort(key=to_str)
lst.sort(key=to_str, reverse=True)
print(lst)

# How would you sort the following list of dictionaries based on the year of publication of each book, from the earliest to the most recent?

books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]
# Expected result
# Pretty printed for clarity
[
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800'
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869'
    },
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967'
    }
]


def sort_book(book):
    return int(book['published'])

print(sorted(books, key=sort_book))
