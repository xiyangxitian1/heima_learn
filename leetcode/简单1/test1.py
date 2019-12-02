class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(i) for i in str(int(''.join(str(i) for i in digits))+1)]




if __name__ == '__main__':
    x = [1, 2, 3, 4]
    x = [9]
    print(Solution().plusOne(x))
