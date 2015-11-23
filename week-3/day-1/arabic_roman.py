print('Hello, I convert arabic number to roman number')
a = int(input('Please add an arabic number (between 1 and 3999): '))
m = a // 1000
m_rest = a % 1000
d = m_rest // 500
d_rest = m_rest % 500
c = d_rest // 100
c_rest = d_rest % 100
l = c_rest // 50
l_rest = c_rest % 50
x = l_rest // 10
x_rest = l_rest % 10
v = x_rest // 5
v_rest = x_rest % 5
i = v_rest
rn = '' #roman number

if a > 3999 or a < 1:
    print('Please add a number between 1 and 3999')
else:
    # 1000
    if m == 3:
        rn += "MMM"
    elif m == 2:
        rn += 'MM'
    elif m == 1:
        rn += 'M'
    else:
        pass
    # 100
    if d == 1 and c == 4:
        rn += 'CM'
    elif d == 1 and c == 3:
        rn += 'DCCC'
    elif d == 1 and c == 2:
        rn += 'DCC'
    elif d == 1 and c == 1:
        rn += 'DC'
    elif d == 1:
        rn += 'D'
    elif d == 0 and c == 4:
        rn += 'CD'
    elif d == 0 and c == 3:
        rn += 'CCC'
    elif d == 0 and c == 2:
        rn += 'CC'
    elif d == 0 and c == 1:
        rn += 'C'
    else:
        pass
    # 10
    if l == 1 and x == 4:
        rn += 'XC'
    elif l == 1 and x == 3:
        rn += 'LXXX'
    elif l == 1 and x == 2:
        rn += 'LXX'
    elif l == 1 and x == 1:
        rn += 'LX'
    elif l == 1:
        rn += 'L'
    elif l == 0 and x == 4:
        rn += 'XL'
    elif l == 0 and x == 3:
        rn += 'XXX'
    elif l == 0 and x == 2:
        rn += 'XX'
    elif l == 0 and x == 1:
        rn += 'X'
    else:
        pass
    # 1
    if v == 1 and i == 4:
        rn += 'IX'
    elif v == 1 and i == 3:
        rn += 'VIII'
    elif v == 1 and i == 2:
        rn += 'VII'
    elif v == 1 and i == 1:
        rn += 'VI'
    elif v == 1:
        rn += 'V'
    elif v == 0 and i == 4:
        rn += 'IV'
    elif v == 0 and i == 3:
        rn += 'III'
    elif v == 0 and i == 2:
        rn += 'II'
    elif v == 0 and i == 1:
        rn += 'I'
    else:
        pass

    print(rn)
