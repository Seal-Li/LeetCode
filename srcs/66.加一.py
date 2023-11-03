#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(map(str, digits))) + 1
        return list(map(int, str(n)))
# @lc code=end