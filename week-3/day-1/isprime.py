isprime = int(input('Enter an integer: '))
n = 2

if isprime < 2:
    if isprime == 1:
        print('Are you "stupid"? It is one, that is no prime. ')
    elif isprime == 0:
        print('It is zero, not prime')
    else:
        print('Negative, please add a positive number')
else:
    while n <= isprime ** 0.5:
        if isprime % n == 0:
            print('No, it\'s no prime')
            break
        n += 1

    else:
        print('Yolo, it is a prime number')
