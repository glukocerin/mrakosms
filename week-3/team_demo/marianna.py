def split(string):
    words_list = string.split(' ')
    return words_list

def long_words(list):
    result_list = []
    for i in list:
        if  len(i) >= 3:
            result_list.append(i)
    return result_list

def is_palindrom(splitted):
    check_list = []
    list_len = len(splitted)
    for item in splitted:
        word = item
        word_len = len(word)
        for i in range(word_len - 2):
            for j in range(i + 3, word_len + 1):
                if word[i:j] == word[i:j][::-1]:
                    check_list.append(word[i:j])
    return check_list

def search_palindromes(string):
    palindromes = []
    words = split(string)
    filter_words = long_words(words)
    palindromes_list = is_palindrom(filter_words)
    palindromes.extend(palindromes_list)
    return (palindromes)

output = search_palindromes('dog goat dad duck doodle never')
print('\nResults of Mariann:\n')
print(output)
