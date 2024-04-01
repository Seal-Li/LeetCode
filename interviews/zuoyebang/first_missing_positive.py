# 缺失的第一个正整数

def first_missing_positive(nums):
    flags = [False] * (len(nums) + 1)
    flags[0] = True

    for num in nums:
        if num > 0 and num <= len(nums):
            flags[num] = True
    
    for i, flag in enumerate(flags):
        if flags == False:
            return i
    return len(nums) + 1

nums = [-1, -2, 3, 4, 5, 1, -5, -6, 2, 7, 6, 60]
print(first_missing_positive(nums))