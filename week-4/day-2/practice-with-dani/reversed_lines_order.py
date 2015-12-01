file_in = open('texts/reversed_zen_order.txt')
file_out = open('texts/reversed_zen_order_out.txt', 'w')


lines = file_in.readlines()
normal_lines = lines[::-1]

output = ''.join(normal_lines)

file_out.write(output)

file_in.close()
file_out.close()
