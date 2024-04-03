def slideWindowMax(nums, k):
    if not nums or len(nums) < k:
        return []
    
    n = len(nums)
    results = []
    for start in range(n-k+1):
        window = nums[start:start+k]
        max_value = window[0]
        for num in window:
            if num > max_value:
                max_value = num
        results.append(max_value)
    return results


def slideWindowMaxOptimal(nums, k):
    if not nums or k == 0:
        return []

    result = []
    deq = []  # 使用列表模拟双端队列

    for i in range(len(nums)):
        # 当新的索引进来时，我们需要保证双端队列的队尾元素对应的值不小于当前考虑的值
        while deq and nums[deq[-1]] < nums[i]:
            deq.pop()

        deq.append(i)

        # 确保双端队列的队首元素在窗口内
        if deq[0] == i - k:
            deq.pop(0)

        # 当窗口形成时，队首元素为当前窗口的最大值
        if i >= k - 1:
            result.append(nums[deq[0]])

    return result


nums = [2, 3, 4, 3, 6, 5, 2, 3]
print(slideWindowMaxOptimal(nums, 3))