# Number is a palindrome if it is equal to the number with digits in reversed order. For example, 5, 44, 171, 4884 are palindromes and 43, 194, 4773 are not palindromes.
# Write a method palindrome_chain_length which takes a positive number and returns the number of special steps needed to obtain a palindrome. The special step is: "reverse the digits, and add to the original number". If the resulting number is not a palindrome, repeat the procedure with the sum until the resulting number is a palindrome.
# If the input number is already a palindrome, the number of steps is 0.
# Input will always be a positive integer.
# For example, start with 87:
# 87 + 78 = 165; 165 + 561 = 726; 726 + 627 = 1353; 1353 + 3531 = 4884
# 4884 is a palindrome and we needed 4 steps to obtain it, so palindrome_chain_length(87) == 4

def make_palindrome(num):
    rev_num = str(num)[::-1]
    return int(rev_num)

def palindrome_sum(num):
    return num + make_palindrome(num)

def round(num):
    palindrome = make_palindrome(num)
    palindrome_round_number = palindrome_sum(palindrome)
    return palindrome_round_number

def is_palindrome_number(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

def palindrome_chain_length(num):
    numbers = []
    while is_palindrome_number(num) == False:
        numbers.append(round(num))
        num = round(num)

    result = len(numbers)
    return result
