# class Soultion:
#
#     def jie(self, x):
#


"""
一共有x树  y个人  就是说  x  = 8 * y + 2, x = 9*y - 5   所以 y = 7 ，  x = 58
如果每人植8棵，则多2棵，
如果每人9棵，则少5棵，问一共多少树？
答： 58棵树
"""

from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')

result = solve([8 * y + 2 - x, x + 5 - 9 * y], [x, y])
print(result)
