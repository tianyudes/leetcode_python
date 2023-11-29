class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if l == r: return nums[l]
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid 
    
solution = Solution()
print(solution.findMin([4,5,6,7,0,1,2]))
print(solution.findMin([3,4,5,1,2]))
print(solution.findMin([11,13,15,17]))
print(solution.findMin([3,1,2]))