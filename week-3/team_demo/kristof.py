import sys
from termcolor import colored

def user_input():
	user_input = input('Enter a string: ')
	return user_input


def menu_input():
	other_input = input('Choose from menu: ')


	try:
		menu_right = False
		while menu_right == False:
			if int(other_input) == 1:
				reverse(user_input())
				menu_right = True
			elif int(other_input) == 2:
				create_palindrome(user_input())
				menu_right = True
			elif int(other_input) == 3:
				search_palindrome(user_input())
				menu_right = True
			elif int(other_input) == 4:
				exit()
			else:
				print('Wrong Input!')
				other_input = input('Choose: ')
			if menu_right == True:
				main()

	except ValueError:
		print('Please only enter numbers! ')
		menu_input()


def reverse(string_input):
	reverse = ''
	for n in string_input:
		reverse = n + reverse
	print('                              ')
	print(colored('\033[47m' + '\033[1m' + 'Your reversed word: ' + reverse, 'red'))

def main():
	user_menu()
	menu_input()

def user_menu():
	print('                                    ')
	print('                                    ')
	print('************************************')
	print('*                                  *')
	print('* 1 Reverse a word                 *')
	print('* 2 Create palindrome              *')
	print('* 3 Search palindrome in a string  *')
	print('* 4 Exit                           *')
	print('*                                  *')
	print('************************************')
	print('                                    ')

def create_palindrome(string_input):
	print('')
	print(colored('\033[47m' + '\033[1m' + string_input + string_input[::-1],'red'))

def search_palindrome(string_input):
	words = string_input.split(' ')
	palindromes = []

	for n in words:
		i2 = 3
		while i2 <= len(n):
			i = 0
			while i <= len(n):
				if n[i:i2] == n[i:i2][::-1] and len(n[i:i2]) >= 3:
					palindromes.append(n[i:i2])
				i += 1
			i2 += 1
	print('')
	print(colored('\033[47m' + '\033[1m' + str(palindromes), 'red'))
