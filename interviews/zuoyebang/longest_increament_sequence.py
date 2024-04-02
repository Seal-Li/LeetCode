def longestIncreamentSequence(nums):
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)

nums = [2, 1, 0, 3, 7, 5, 11, 15, 6, 17, 20, 19]
print(longestIncreamentSequence(nums))