def unique_in_order(iterable):
    output = []
    output.append(iterable[0])
    x = 1
    for i in range(len(iterable)):
        if iterable[i] == output[i - x]:
            pass
        else:
            output.append(iterable[i])
        x += 1
    return output
