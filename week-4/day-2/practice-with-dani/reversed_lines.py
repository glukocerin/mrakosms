file_in = open('texts/reversed_zen_lines.txt')
file_out = open('texts/reversed_zen_lines_out.txt', 'w')

output = ''
for line in file_in:
    line = line.rstrip()
    new_line = line[::-1]
    output += new_line + '\n'

file_out.write(output)


file_in.close()
file_out.close()
