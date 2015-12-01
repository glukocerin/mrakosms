def rot13(message):
    output = ''

    for word in message:
        for char in word:
            if ord(char) < 65 or ord(char) > 122:
                output += char
            elif ord(char) < 97 and ord(char) > 90:
                output += char
            else:
                if ('A' <= char and char <= 'M') or ('a' <= char and char <= 'm'):
                    output += chr(ord(char) + 13)
                else:
                    output += chr(ord(char) - 13)
    print(output)
    return output






print(rot13('EBG 13 rknzcyr.'))

    #13-mal eltolva
