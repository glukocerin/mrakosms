roman_number = input('Please type a Roman number: ').upper()
rn = roman_number
rn = rn.replace('M', '1000 ' )
rn = rn.replace('D', '500 ')
rn = rn.replace('C', '100 ')
rn = rn.replace('L', '50 ')
rn = rn.replace('X', '10 ')
rn = rn.replace('V', '5 ')
rn = rn.replace('I', '1 ')
rn = rn.split()
rn = list(map(int, rn))
rn.append(0) # last element
num = len(rn) # max 15
i = 0

for i in range(i-1, num):
    if int(rn[i-1]) < int(rn[i]):
        rn[i-1] = -(rn[i-1])
    i += 1
else:
    pass

print('I convert your Roman number (', roman_number, ') to Arabic number:', (sum(rn)), sep='')

# need features -check only valid, check lenght max 15
