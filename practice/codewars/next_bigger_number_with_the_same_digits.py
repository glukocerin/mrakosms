# def next_bigger(num):
#     numlist = [int(i) for i in str(num)]

#     index_of_replace_num = -1
#     i = len(numlist) - 1
#     while i > 0:
#         if numlist[i] > numlist[i-1]:
#             index_of_replace_num = i - 1
#             break
#         i -= 1

#     if index_of_replace_num == -1:
#         return -1
#     else:
#         firstlist = numlist[:index_of_replace_num]
#         replaced_num = numlist[index_of_replace_num]
#         secondlist = numlist[index_of_replace_num+1:]
#         new_replaced_num = 9
#         i = 0
#         delindex = 0
#         while i < len(secondlist):
#             if secondlist[i] > replaced_num and secondlist[i] < new_replaced_num:
#                 new_replaced_num = secondlist[i]
#                 delindex = i
#             i += 1

#         secondlist.pop(delindex)
#         secondlist.append(replaced_num)
#         firstlist.append(new_replaced_num)
#         output = firstlist + sorted(secondlist)
#         return int(''.join(str(x) for x in output))

# http://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# It is more compactly.

def next_bigger(num):
    digits = [int(i) for i in str(num)]

    i = len(digits) - 1
    while i > 0 and digits[i - 1] >= digits[i]:
        i -= 1
    if i <= 0:
        return -1

    swap_idx = len(digits) - 1
    while digits[swap_idx] <= digits[i - 1]:
        swap_idx -= 1
    digits[i - 1], digits[swap_idx] = digits[swap_idx], digits[i - 1]

    digits[i : ] = digits[len(digits) - 1 : i - 1 : -1]
    return int(''.join(str(x) for x in digits))

# http://codereview.stackexchange.com/questions/115609/next-bigger-number-with-the-same-digits

def swap_first_with_higher(digits):
    """
    >>> swap_first_with_higher(list('59853'))
    ['8', '9', '5', '5', '3']

    """
    for pos in range(len(digits) - 1, 0, -1):
        if digits[0] < digits[pos]:
            digits[0], digits[pos] = digits[pos], digits[0]
            break
    return digits


def reversed_tail(digits):
    """
    >>> reversed_tail(list('89553'))
    ['8', '3', '5', '5', '9']

    """
    return [digits[0]] + digits[1:][::-1]


def next_biggest(num):
    """
    >>> next_biggest(59853)
    83559

    >>> next_biggest(111)
    -1

    >>> next_biggest(11211)
    12111

    """
    digits = list(str(num))
    for pos in range(len(digits) - 1, 0, -1):
        if digits[pos-1] < digits[pos]:
            left = digits[:pos-1]
            right = reversed_tail(swap_first_with_higher(digits[pos-1:]))
            return int(''.join(left + right))

    return -1
