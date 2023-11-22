#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = nums[0]
        flag = 1
        for ele in nums[1:]:
            if ele == val:
                flag += 1
            else:
                if flag == 0:
                    val = ele
                    flag =1
                else:
                    flag -= 1
        return val
# @lc code=end

