# http://www.codewars.com/kata/55f3facb78a9fd5b26000036/train/python
# While surfing in web I found interesting math problem called "Always perfect". That means if you add 1 to the product of four consecutive numbers the answer is ALWAYS a perfect square. For example we have: 1,2,3,4 and the product will be 1X2X3X4=24.
# If we add 1 to the product that would become 25, since the result number is a perfect square the square root of 25 would be 5. So now lets write a function which takes numbers separated by commas in string format and returns the number which is a perfect square and the square root of that number.
# If string contains other characters than number or it has more or less than 4 numbers separated by comma function returns "incorrect input".
# If string contains 4 numbers but not consecutive it returns "not consecutive”.’''

def always_perfect(string): # always_perfect('1,2,3,4')
    numbers = string.split(',')
    number_list = []
    for n in numbers:
        number_list.append(n)

    if 'a' in number_list or len(number_list) != 4:
        return 'incorrect input'

    number_list = list(map(int, number_list))

    for i in range(min(len(numbers), 3)):
        if number_list[i] + 1 != number_list[i+1]:
            return 'not consecutive'

    amount = 1
    for n in numbers:
        amount *= int(n)

    product = (amount + 1) ** 0.5
    result = amount + 1, int(product)
    return result
