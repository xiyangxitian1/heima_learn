# 有效的括号 () [] {}
# 1.有多个( 就要相应的有多少个)
# 2.要相应的括号 中间不能放其他的不闭合的　如 (]) 这种是不可以的
# 3.怎么解呢，     从第一个开始， [([])]([])
class Solution:
    def isValid(self, s: str) -> bool:
        left = '([{'
        right = ')]}'
        dict1 = {'(': ')', '[': ']', '{': '}'}
        stack = []
        if len(s) % 2 != 0:
            return False
        for s1 in s:
            if s1 in left:
                stack.append(s1)
            elif stack and dict1.get(stack.pop()) != s1:
                return False

        return len(stack) == 0


if __name__ == '__main__':
    x = '[([])]([])'
    # x = "()[]{}"
    # x = "}"
    x = '){'
    print(Solution().isValid(x))
