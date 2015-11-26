# 1st Part:
#
# Create a function that takes a string and creates a palindrome from it.
# It should work like this:
#
# output = create_palindrome('pear')
#
# print(output) # it prints: pearraep

def create_palindrome(word):
    return word + word[::-1]

output = create_palindrome('pear')
print(output)
