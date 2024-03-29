def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    middle = (left + right) // 2

    while left < right:
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
        middle = (left + right) // 2
    return "target value not exists in this nums"

nums = [1, 3, 5, 6, 7, 8, 10, 12, 15, 21, 30, 50]
print(binary_search(nums, 10))