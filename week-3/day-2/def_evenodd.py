def is_even(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'

num = int(input('Number: '))

print(is_even(num))
