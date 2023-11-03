#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[pos] = nums[i]
                pos += 1
        return pos
# @lc code=end

