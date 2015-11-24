rn = input('Roman number: ')
rn = rn.upper()

print(rn)
chars = set('[~?!@#$%^&*()_+{}":;\'ABEFGHJKNOPQRSTUWYZ]+$')

if any((c in chars) for c in str(rn)): #valid characters?
    print('Please use only valid characters! M-D-C-L-X-V-I') # no valid characters
else:
    print('mehet')
