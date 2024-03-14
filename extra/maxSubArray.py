def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 初始化当前子数组的最大和为数组的第一个元素
    current_max = nums[0]
    # 初始化全局最大和也为数组的第一个元素
    global_max = nums[0]
    
    # 从数组的第二个元素开始遍历
    for i in range(1, len(nums)):
        # 更新当前子数组的最大和
        # 如果当前子数组的最大和加上当前元素的值比当前元素的值小，
        # 那么就从当前元素开始重新计算子数组的最大和
        current_max = max(nums[i], current_max + nums[i])
        
        # 更新到目前为止所有子数组的最大和
        global_max = max(global_max, current_max)
    
    return global_max