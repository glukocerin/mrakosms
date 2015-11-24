# R(0) = 0
# R(1) = 1
# R(2) = 1

def fibo(n):
    if n == 0:
        return 0
    if n== 1:
        return 1
    return fibo(n-1)+fibo(n-2)

res = fibo(3)
print(res)
