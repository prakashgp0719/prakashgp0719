a = input('get input for addition press 1 or subtraction press 2:')
if a == '1' or a == '2':
    if a == '1':
        print('you selected addition')
    elif a == '2':
        print('you selected subraction')
    else:
        print('wrong')
    b = int(input('get input for number of bit:'))
    print(b)

    c = input('A=')
    e = list(c)
    g = len(e)

    d = input('B=')
    f = list(d)
    h = len(f)
    if b == g and b == h:
        if a == '1':
            sum = bin(int(c, 2) + int(d, 2))
            print('output is', sum)
        elif a == '2':
            diff = bin(int(c, 2) - int(d, 2))
            print('output is', diff)
    else:
        print('sorry! you selected wrong.Please select once again')
else:
    print('please only select 1 or 2')