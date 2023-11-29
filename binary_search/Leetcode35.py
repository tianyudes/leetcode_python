class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1 

        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] == target: return mid
            elif nums[mid] < target: l = mid + 1
            else: r = mid

        if nums[l] >= target: return l
        elif nums[r] >= target: return r 
        else: return r + 1         


solution = Solution()
print(solution.searchInsert(nums = [1,3,5,6], target = 2))
print(solution.searchInsert(nums = [1,3,5,6], target = 5))
print(solution.searchInsert(nums = [1,3,5,6], target = 7))

