# /3 fizz
# /5 buzz
# /3 & /5 fizzbuzz
# contain 5 buzzfizz

n = 0
max = int(input('Enter a number: '))

while n < max:
    if n % 3 == 0 and n %5 == 0:
        print(n, ':fizzbuzz')
    elif n % 3 == 0:
        print(n, ':buzz')
    elif n % 5 == 0:
        print (n, ':fizz')
    elif '5' in str(n):
        print(n, ':buzz')
    else:
        print(n)
    n += 1
