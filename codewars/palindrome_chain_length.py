# Number is a palindrome if it is equal to the number with digits in reversed order. For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.
# Write a method palindrome_chain_length which takes a positive number and returns the number of special steps needed to obtain a palindrome. The special step is: "reverse the digits, and add to the original number". If the resulting number is not a palindrome, repeat the procedure with the sum until the resulting number is a palindrome.
# If the input number is already a palindrome, the number of steps is 0.
# Input will always be a positive integer.
# For example, start with 87:
# 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884
# 4884 is a palindrome and we needed 4 steps to obtain it, so palindrome_chain_length(87) == 4

def make_palindrome(number):
    number_reverse = str(number)[::-1]
    return int(number_reverse)

def palindrome_sum(number):
    return number + make_palindrome(number)

def round(number):
    palindrome = make_palindrome(number)
    palindrome_round_number = palindrome_sum(palindrome)
    return palindrome_round_number

def is_palindrome_number(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

def palindrome_chain_length(start_number):
    actual_number = start_number
    numbers_list = []
    while is_palindrome_number(actual_number) == False:
        numbers_list.append(round(actual_number))
        actual_number = round(actual_number)

    result = len(numbers_list)
    return result
