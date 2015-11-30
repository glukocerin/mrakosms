def test(expected, actual, message):
    if expected == actual:
        print('check')
    else:
        print('Error: ' + message)
        print(expected, actual)

TOKENS = {
    '5': 'V'
    '4': 'IV'
    '1': 'I'
}

def arabic2roman(arabic):
    output = ''
    biggest_token = 0
    while arabic > 0:
        if arabic == 5

            output += TOKENS[str(arabic)]
            arabic -= 5
        if arabic == 4:
            output += TOKENS[str(arabic)]
            arabic -= 4
        output += 'I' * arabic
        arabic = 0
    return output




test(arabic2roman(0), '', 'it should be handle 0')
test(arabic2roman(1), 'I', 'it should be handle 1')
test(arabic2roman(2), 'II', 'it should be handle 3')
test(arabic2roman(4), 'IV', 'it should be handle 4')
test(arabic2roman(5), 'V', 'it should be handle 5')
test(arabic2roman(6), 'VI', 'it should be handle 6')
test(arabic2roman(7), 'VI', 'it should be handle 7')
