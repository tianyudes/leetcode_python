class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        target_index = self.findTarget(nums, target)
        if target_index == -1: return [-1, -1]
        start, end = target_index, target_index
        while start-1>=0 and nums[start-1] == target:
            start -= 1
        while end+1 <= len(nums) - 1 and nums[end+1] == target:
            end += 1
        return [start, end]

    def findTarget(self, nums, target):
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: l = mid + 1
            else: r = mid - 1
        return -1
    
solution = Solution()
print(solution.searchRange([5,7,7,8,8,10], 0))