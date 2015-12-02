# def wc(filename):
#     file_in = open(filename)
#     text = file_in.read()
#     lines = len(text.split('\n'))
#     chars = len(text)
#     file_in.close()
#     return [lines, chars]
#
# print(wc('alma.txt'))
#
# def last(f_arg, *argv):
#     return arg[-1]


def last(*x):
    if type(x[-1]) == list or type(x[-1]) == str or type(x[-1]) == tuple:
        return x[-1][-1]
    else:
        return x[-1]


print(last('abckxyz',))
