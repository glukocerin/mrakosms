def greet(name):
    return 'Hello, ' + name

result = greet('Akos')
print(result)

g = []
def add(a, b):
    res = a + b
    g.append(res)
    return res

def add(a, b):
    global n
    n = a + b

add(1, 2)
print(n)

print (add(1, 2))
print (add(7, 2))
print(g)

n = 1
def my_print():
    n = 2
    print(n)

my_print(
)

def add(a, b, res = None):
    if res is None:
        res = []
    r = a + b
    res.append(r)
    print(res)
    return r

add(1,2)
add(2,3)
add(4,5)
