#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 1
        val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > val:
                nums[pos] = nums[i]
                val = nums[i]
                pos += 1
            else:
                continue
        return pos

# @lc code=end

