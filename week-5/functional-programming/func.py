# map

# def adder(array):
#     output = []
#     for i in array:
#         output.append(i+1)
#     return output

def adder(array):
    return list(map(lambda n : n + 1, array))


# Genarator
# def map(func, array):
#     for i in array:
#         yield func(i)

# filter

# def filter_array(array):
#     output = []
#     for i in array:
#         if i % 3 == 0:
#             output.append(i)
#     return output

def filter_array(array):
    return list(filter(lambda n : n % 3 == 0, array))
