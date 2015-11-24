print('Hello, I convert arabic number to roman number')
an = int(input('Please add an arabic number (between 1 and 3999): '))
# an = arabic number
m = an // 1000
m_rest = an % 1000
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

if an > 4000 or an < 0:
    print('Please add a number between 1 and 3999')
else:
    # Thousands
    if m == 3: # 3000
        rn += "MMM"
    elif m == 2: # 2000
        rn += 'MM'
    elif m == 1: # 1000
        rn += 'M'
    else:
        pass
    # hundreds
    if d == 1 and c == 4: # 900
        rn += 'CM'
    elif d == 1 and c == 3: # 800
        rn += 'DCCC'
    elif d == 1 and c == 2: # 700
        rn += 'DCC'
    elif d == 1 and c == 1: # 600
        rn += 'DC'
    elif d == 1: # 500
        rn += 'D'
    elif d == 0 and c == 4: # 400
        rn += 'CD'
    elif d == 0 and c == 3: # 300
        rn += 'CCC'
    elif d == 0 and c == 2: # 200
        rn += 'CC'
    elif d == 0 and c == 1: # 100
        rn += 'C'
    else:
        pass
    # tens
    if l == 1 and x == 4: # 90
        rn += 'XC'
    elif l == 1 and x == 3: # 80
        rn += 'LXXX'
    elif l == 1 and x == 2: # 70
        rn += 'LXX'
    elif l == 1 and x == 1: # 60
        rn += 'LX'
    elif l == 1: # 50
        rn += 'L'
    elif l == 0 and x == 4: # 40
        rn += 'XL'
    elif l == 0 and x == 3: # 30
        rn += 'XXX'
    elif l == 0 and x == 2: # 20
        rn += 'XX'
    elif l == 0 and x == 1: # 10
        rn += 'X'
    else:
        pass
    # ones
    if v == 1 and i == 4: # 9
        rn += 'IX'
    elif v == 1 and i == 3: # 8
        rn += 'VIII'
    elif v == 1 and i == 2: # 7
        rn += 'VII'
    elif v == 1 and i == 1: # 6
        rn += 'VI'
    elif v == 1: # 5
        rn += 'V'
    elif v == 0 and i == 4: # 4
        rn += 'IV'
    elif v == 0 and i == 3: # 3
        rn += 'III'
    elif v == 0 and i == 2: # 2
        rn += 'II'
    elif v == 0 and i == 1: # 1
        rn += 'I'
    else:
        pass

    print('I converted your Arabic number (', an, ') to Roman number (', rn ,').', sep='')
