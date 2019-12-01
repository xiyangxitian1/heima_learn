class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if '.' not in p and '*' not in p:
            if s != p:
                return False
            else:
                return True
        elif '*' not in p:
            if len(s) != len(p):
                return False
            else:
                dict1 = dict(zip(list(s), list(p)))
                for k, v in dict1.items():
                    if k != v and v != '.':
                        return False
        elif '.' not in p:
            pass
        else:  # . * 都在p里
            pass


        return True


if __name__ == '__main__':
    s = 'abcde'
    p = 'a*.de'
    result = Solution().isMatch(s, p)
    print(result)
