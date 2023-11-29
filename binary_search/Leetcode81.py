class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r-l) // 2  # !!
            if nums[mid] == target: return True

            while l < mid and nums[l] == nums[mid]:
                l += 1
            while r > mid and nums[r] == nums[mid]:
                r -= 1

            if nums[l] <= nums[mid]:
                if nums[l] <=target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else: 
                    r = mid - 1 
        return False

solution = Solution()
print(solution.search([1,0,1,1,1], 0))