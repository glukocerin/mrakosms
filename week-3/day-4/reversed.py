list = [1,2,3,4,5]

def reversed(sorted):
    output = []
    i = 0
    max = len(sorted)
    while i < max:
        output.append(sorted[-i-1])
        i += 1
    return output
