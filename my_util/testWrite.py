f = open('a.txt', 'w')
l = ['hello', 'god']

f.writelines('\n'.join(l))

f.close()
