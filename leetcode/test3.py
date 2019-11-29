class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        lookup = set()
        left = 0
        cur_len = 0
        max_len = 0
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
