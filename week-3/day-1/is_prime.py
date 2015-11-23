is_prime = int(input('Enter an integer: '))
n = 2

if is_prime < 2:
    if is_prime == 1:
        print('Are you "stupid"? It is one, that is no prime. ')
    elif is_prime == 0:
        print('It is zero, not prime')
    else:
        print('Negative, please add a positive number')
else:
    while n <= is_prime ** 0.5:
        if is_prime % n == 0:
            print('No, it\'s no prime')
            break
        n += 1

    else:
        print('Yolo, it is a prime number')
