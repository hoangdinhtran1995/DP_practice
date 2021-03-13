
def list_xorer():
    print('Q to stop\n"0 X" to add X to list\n"1 X" to xor every element in list\n')
    lst = []

    running = True
    while running:
        inp = input()

        if inp[0:2] == '0 ':
            lst.append(int(inp[2:]))


        if inp[0:2] == '1 ':
            X = int(inp[2:])
            for i in range(len(lst)):
                lst[i] ^= X

        if inp == 'Q':
            running = False

        print('Current list: ', lst)
