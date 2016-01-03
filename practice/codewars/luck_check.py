def luck_check(string):
    first = 0
    for n in range(0, int(len(string) / 2 ) ):
        first += int(string[n])
    second = 0
    if len(string) % 2 == 0:
        for n in range(int(len(string) / 2 ),len(string)):
            second += int(string[n])
    else:
        for n in range(int(len(string) / 2 + 1 ),len(string)):
            second += int(string[n])

    if first == second:
        return True
    return False
