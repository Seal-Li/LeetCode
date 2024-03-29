def find_secondary_number_no_repeat(nums):
    '''
    不将重复的最大值作为第二大的数字
    '''
    if len(nums) < 2:
        return None
    
    first = max(nums[0], nums[1])
    second = min(nums[0], nums[1])

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:  # 排除重复的最大值
            second = num
    return second


def find_secondary_number_repeat(nums):
    '''
    将重复的最大值作为第二大的数字
    '''
    if len(nums) < 2:
        return None
    
    first = max(nums[0], nums[1])
    second = min(nums[0], nums[1])

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second:  # 排除重复的最大值
            second = num
    return second


nums = [10, 2, 5, 7, 3, 1, 0, 4, 9, 10]
print(find_secondary_number_no_repeat(nums))
print(find_secondary_number_repeat(nums))