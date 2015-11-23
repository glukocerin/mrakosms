
print('It\'s magic! I will show you the prime numbers. Please type in the start and finish numbers.')
prime = int(input('First number: '))
last = int(input('Last number: '))

print('The prime numbers between', prime, 'and', last)
for prime in range(prime, last+1):
    if prime >= 2:
        for divider in range(2,prime):
            if prime % divider == 0:
                break
            divider +=1
        else:
            print(prime)
    else:
        pass
