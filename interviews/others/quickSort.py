def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    
    pivot = nums[0]
    left = [num for num in nums if num < pivot]
    middle = [num for num in nums if num == pivot]
    right = [num for num in nums if num > pivot]

    return quick_sort(left) + middle + quick_sort(right)


nums = [9, 6, 3, 1, 7, 9, 12, 13, 5, 2, 6, 8, 15, 21]
print(quick_sort(nums))