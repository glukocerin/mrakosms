# 2nd Part:
#
# Create a function that searches for all the palindromes in a string that are longer than 3 characters, and returns a list with the found palindromes. Example:
#
# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['dad', 'dood', 'eve']

# lilli?

def cut_palindrones_input_string(string):
    words = string.split(' ')
    return words

def is_palindromes_lenght_valid(word):
    if len(word) >= 3:
        return True

def is_palindromes(word):
    try:
        if is_palindromes_lenght_valid(word):
            i = 0
            for i in range(0, len(word)-1):
                if word[i] == word[i+2]:
                    return True
                elif word[i] == word[i+1] and word[i-1] == word[i+2]:
                    return True
            return word
    except IndexError:
        pass

def palindrome_length(word):
    palindrome = ''
    for i in range(1, len(word)-1):
        if word[i] == word[i+1]:
            palindrome = word[i] + word[i+1]
            if word[i-1] == word[i+2]:
                palindrome = word[i-1] + palindrome + word[i+2]
                


    print(palindrome)


def search_palindromes(string):
    wordslist = cut_palindrones_input_string(string)
    i = 0
    while i < len(wordslist):
        if is_palindromes(wordslist[i]):
            print(wordslist[i])
        i += 1

search_palindromes(input('Adj meg valamit: '))
