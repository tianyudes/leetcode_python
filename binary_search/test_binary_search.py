def binary_search_first_occurance(nums, target):
    l ,r = 0, len(nums) - 1
    res = -1
    while l <= r:
        mid = l + (r-l) // 2
        if nums[mid] == target:
            res = mid
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return res

def binary_search_last_occurance(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = l + (r - l) // 2  
        if nums[mid] == target:
            res = mid
            l = mid + 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return res





a = [1,1,1,2,6,7]
a = [1,1,1,2,2,2,3]
print(binary_search_first_occurance(a, 2))
print(binary_search_last_occurance(a, 2))
