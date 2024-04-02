def threeNumsSum(nums):
    nums.sort()
    results = []

    for i in range(len(nums)-2):
        left = i + 1
        right = len(nums) - 1

        if nums[i] > 0:
            break
        if nums[i] == nums[i-1]:
            continue

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total > 0:
                right -= 1
            elif total < 0:
                left += 1
            else:
                results.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return results
    
nums = [-1, 0, 1, 2, -1, -4]
print(threeNumsSum(nums))