#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)
        middle = (start + end) // 2
        while start < end:
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else:
                end = middle
            middle = (start + end) // 2
        return start
# @lc code=end

