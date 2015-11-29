

def user_input():
	a = input('add meg a szoveget!: ')
	b = int(input('add meg szamot'))
	return word_splitter(a, b)

def word_splitter(string, length_of_palindrom):
	n = length_of_palindrom
	if not string or not length_of_palindrom:
		print('empty argumentum please fill it!')
	else:
		words_list = string.split(' ')
		return list_count(words_list, n)

def list_count(list, n):
	new_list  = []
	for item in list:
		if len(item) >= n:
			if check_palindrome(item, n):
				new_list.append(item)
	return print(new_list)

def check_palindrome(word, n):
	palindrom_list = []
	word_length = len(word)
	for i in range(word_length):
		for j in range(word_length):
			if word[i:j+1] == word[i:j+1][::-1] and len(word[i:j+1]) > n-1:
				palindrom_list.append(word[i:j+1])
				print(palindrom_list)
				return word
