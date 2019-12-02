class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str1 = s.rstrip()
        if not str1:
            return 0
        count = 0
        for i in range(len(str1) - 1, 0, -1):
            if str1[i] != ' ':
                count += 1
            else:
                return count
        else:
            return count
