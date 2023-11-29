class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < numRows: return s
        res = ["" for i in range(numRows)]
        index, step = 0, 0
        for ch in s:
            res[index] += ch
            if index == 0:
                step = 1
            if index == numRows - 1:
                step = -1
            index += step
        return "".join(res)
            


solution = Solution()
print(solution.convert("PAYPALISHIRING", 3))