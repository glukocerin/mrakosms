# af = 123
#
# def double(num):
#     return num * 2
#
# af = double(af)
#
# print(af)
#
# *****************
#
# ag = 'kuty'
#
# def join_character(string):
#     return string + 'a'
#
# ag = join_character(ag)
#
# print(ag)
#
# *****************
#
# ag2 = ['rep', 'macsk', 'cic', 'alm', 'Ann', 'kacs']
#
# for i in range(len(ag2)):
#     ag2[i] = join_character(ag2[i])
#
# print(ag2)

numbers = [4, 5, 6, 7, 8, 9, 10]
#
# def sum_numbers(numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     return result
#
# print(sum_numbers(numbers))
#
# def sum_numbers(numbers):
#     return

def factorial_1(num):
    factorial = 1
    i = 1
    while i <= num:
        factorial *= i
        i += 1
    return factorial

# print(factorial_1(6))

def factorial_2(num): # recursive
    if num == 1:
        return 1
    else:
        return num * factorial_2(num-1)

print(factorial_2(6))

def factorial_3(num):
    factorial = 1
    for n in range(1, num+1):
        factorial *= n
    return factorial

# print(factorial_3(6))
