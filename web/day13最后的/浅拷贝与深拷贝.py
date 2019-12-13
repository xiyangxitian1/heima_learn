b = [1, 2, 3]
a = b
print(id(a))

b[0] = 100
b.append(30)
b.remove(100)
print(id(b))
