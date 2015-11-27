# 2nd Part:
#
# Create a function that searches for all the palindromes in a string that are longer than 3 characters, and returns a list with the found palindromes. Example:
#
# output = search_palindromes('dog goat dad duck doodle never')
# print(output) # it prints: ['dad', 'dood', 'eve']

# Test 'dad balabala doodle never duck goat dog dad balabalal'

def create_palindromes_list(string):
    wordslist = string.split(' ')
    return wordslist

def is_palindromes_lenght_valid(word):
    if len(word) >= 3:
        return word

def create_palindromes_wordlist(string):
    wordslist = create_palindromes_list(string)
    wordlist = []
    for word in wordslist:
        if is_palindromes_lenght_valid(word):
            wordlist.append(word)
    return wordlist

def show_palindrome(word):
    palindromes = []
    wordlength = len(word)
    for i in range(wordlength):
        for j in range(wordlength):
            if word[i:j+1] == word[i:j+1][::-1] and len(word[i:j+1]) > 2:
                palindromes.append(word[i:j+1])
    return palindromes

def search_palindromes(string):
    startlist = create_palindromes_wordlist(string)
    output_temp = []
    for word in startlist:
        output_temp.extend(show_palindrome(word))

    output = set(output_temp)
    return output
