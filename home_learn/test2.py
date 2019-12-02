with open('../my_util/pwd.txt', 'r') as f:
    a = f.read()
    if '3pn9tse6' in a:
        print('ok')
    else:
        print('no')