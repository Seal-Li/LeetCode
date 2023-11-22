#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        for ele in nums:
            if ele in hash_map:
                hash_map[ele] += 1
            else:
                hash_map[ele] = 1
        for key, value in hash_map.items():
            if value == 1:
                return key
# @lc code=end

