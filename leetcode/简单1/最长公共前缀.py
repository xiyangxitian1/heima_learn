class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ''
        if len(strs) == 1:
            return strs[0]
        s = ""
        for i in zip(*strs):
            # print(i)
            if len(set(i)) == 1:
                s += i[0]
            else:
                break
        return s

    # 输入: ["flower","flow","flight"]


# 输出: "fl"


if __name__ == '__main__':
    x = ["flower", "flow", "flight"]
    # x = ["c", "c"]
    print(Solution().longestCommonPrefix(x))
