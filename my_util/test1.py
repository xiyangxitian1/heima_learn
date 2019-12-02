with open('./pwd.txt', 'r') as f:
    a = f.readline()
    if '\n' in a:
        a = a.replace('\n', '')
