class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t) < len(s): return False

        index_s, index_t = 0, 0
        while index_s < len(s) and index_t < len(t):
            if s[index_s] == t[index_t]:
                index_s += 1
                index_t += 1
            else:
                index_t += 1

        return index_s == len(s)
    
solution = Solution()
print(solution.isSubsequence(s = "abc", t = "ahbgdc"))