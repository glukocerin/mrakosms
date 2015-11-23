fibonacci = [0, 1]
i = 0

last = int(input('How many fibonacci numbers would you like to see? Enter the number: '))

for i in range(0, last-2):
    num = len(fibonacci)
    fibonacci.append(fibonacci[num-1]+fibonacci[num-2])
print(fibonacci)
