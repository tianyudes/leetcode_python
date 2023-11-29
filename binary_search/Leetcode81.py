class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1


solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 0))