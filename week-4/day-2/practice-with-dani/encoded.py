file_in = open('texts/encoded_zen_lines.txt')
file_out = open('texts/encoded_zen_lines_out.txt', 'w')
# chr(int)
#
# ord(str)

for line in file_in:
    lines = line.rstrip()
    words = lines.split()

    encoded_words = []
    for word in words:
        encoded_word = ''
        for char in word:
            encoded_word += chr(ord(char) - 1)

        encoded_words.append(encoded_word)

    encoded_line = ' '.join(encoded_words)
    file_out.write(encoded_line + "\n")


file_in.close()
file_out.close()
