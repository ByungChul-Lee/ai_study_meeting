num_of_asterisk = 6
num_of_space = 1
while num_of_asterisk >= 0:
    for i in range(num_of_space):
       print(' ', end="")
    for i in range(num_of_asterisk * 2):
       print('*', end="")
    print("\n")
    num_of_asterisk = num_of_asterisk - 1
    num_of_space = num_of_space + 1