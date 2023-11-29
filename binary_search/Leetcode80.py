class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[res - 2]:
                nums[res] = nums[i]
                res += 1
        return res


def main():
    solution = Solution()
    nums = [1,1,1,2,3,3,3,4,5]
    k = solution.removeDuplicates(nums)
    print(k)


if __name__ == "__main__":
    main()