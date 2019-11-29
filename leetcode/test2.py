# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         if not s:
#             return 0
#         left = 0
#         lookup = set()
#         n = len(s)
#         max_len = 0
#         cur_len = 0
#         for i in range(n):
#             cur_len += 1
#             while s[i] in lookup:
#                 lookup.remove(s[left])
#                 left += 1
#                 cur_len -= 1
#             if cur_len > max_len:
#                 max_len = cur_len
#             lookup.add(s[i])
#             #  aabcdeageg
#         return max_len
#
# 作者：powcai
# 链接：https: // leetcode - cn.com / problems / longest - substring - without - repeating - characters / solution / hua - dong - chuang - kou - by - powcai /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        max_len = 0
        cur_len = 0
        for i in s:
            cur_len += 1
            while i in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(i)
        return max_len


if __name__ == '__main__':
    s1 = Solution()
    result = s1.lengthOfLongestSubstring('aabcdeageg')
    print(result)
