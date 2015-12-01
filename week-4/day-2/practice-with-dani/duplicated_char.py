file_in = open('texts/duplicated_chars.txt')
file_out = open('texts/duplicated_chars_out.txt', 'w')



lines = file_in.readlines()
output = ''
for line in lines:
    if line == '\n':
        output += line
    else:
        output += line[::2]
file_out.write(output)


file_in.close()
file_out.close()
