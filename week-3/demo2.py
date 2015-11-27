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
            if word[i:j+1] == word[i:j+1][::-1] and len(word[i:j+1]) >= 2:
                palindromes.append(word[i:j+1])
    return palindromes

def search_palindromes(string):
    startlist = create_palindromes_wordlist(string)
    output_temp = []
    for word in startlist:
        output_temp.extend(show_palindrome(word))

    output = set(output_temp)

    print('Found the following palindromes in the text: \n', output)

def create_palindrome(word):
    output = word + word[::-1]
    print('The palindrome of', word, 'is:', output)

def menu():
    choose = input('Please choose the following menu: \n 1 - Create Palindrome \n 2 - Search Palindromes in a text \n Q - quit the menu \n Type the number or quit: ').lower()
    while choose != 'q':
        if choose == '1':
            create_palindrome(input('\n****************************************\n \n Please type a word: '))
        if choose == '2':
            search_palindromes(input('Please type: '))
        choose = input('Super! What is next? \n Choose the following menu: \n 1 - Create Palindrome \n 2 - Search Palindromes in a text \n Q - quit the menu \n Type the number or quit: ').lower()

menu()
