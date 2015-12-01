from awesome.reverse import reverse_list

import os

print(reverse_list([1, 2, 3, 4, 5]))

print(os.getpid())
print(os.getuid())
print(os.getcwd())

alma_file = open('alma.txt', 'w')
alma_file.write('Balozskam')
alma_file.close()
