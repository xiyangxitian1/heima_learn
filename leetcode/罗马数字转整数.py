# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# 有以下3种特殊情况
# I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
# X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
# C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

# 想法：把 IV 用A表示 A=4      IX 用B=9
#         XL = E = 40         XC = F = 90
#          CD = G = 400       CM = H = 900
#  这样替换后每个字母表示一个数字，然后相加得到和就可以了
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
class Solution:
    def romanToInt(self, s: str) -> int:
        dict1 = {'I': 1, 'A': 4, 'V': 5, 'B': 9, 'X': 10, 'E': 40, 'L': 50, 'F': 90, 'C': 100,
                 'G': 400, 'D': 500,
                 'H': 900, 'M': 1000}
        return sum([dict1[i] for i in s.replace('IV', 'A').replace('IX', 'B').replace('XC', 'F') \
                   .replace('CD', 'G').replace('CM', 'H').replace('XL', 'E')])

if __name__ == '__main__':
    x = 'IX'
    x = "MMMXLV"  # 1000+1000+1000+40+5  = 3045
    print(Solution().romanToInt(x))
