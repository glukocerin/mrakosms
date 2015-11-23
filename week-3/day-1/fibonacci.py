fibonacci = [0, 1]
i = 0

for i in range(0, 10):
    a = len(fibonacci)
    fibonacci.append(fibonacci[a-1]+fibonacci[a-2])
print(fibonacci)
