class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l, r = 1, x 
        while l <= r:
            mid = l + (r - l) //2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
        return l - 1


solution = Solution()
print(solution.mySqrt(8))
