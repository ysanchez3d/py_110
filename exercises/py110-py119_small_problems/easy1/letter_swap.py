# Letter Swap
# Given a string of words separated by spaces, write a function that swaps the first and last letters of every word.

# You may assume that every word contains at least one letter, and that the string will always contain at least one word. You may also assume that each string contains nothing but words and spaces, and that there are no leading, trailing, or repeated spaces.


def swap(string):
    words = string.split(" ")

    for idx, word in enumerate(words):
        word_length = len(word)
        if word_length == 1:
            continue
        
        new_word = word[-1] + word[1:-1] + word[0]
        words[idx] = new_word
 
    return " ".join(words)

# Examples
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
