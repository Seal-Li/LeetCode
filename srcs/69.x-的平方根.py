#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:  # sourcery skip: avoid-builtin-shadow
        if x == 1:
            return 1
        start = 0
        end = x
        # print(end)
        while True:
            # print(start, end)
            middle = (start + end) // 2
            cur = middle * middle
            next = (middle + 1) * (middle + 1)
            if (cur <= x) and (next > x):
                return middle
            elif next == x:
                return middle + 1
            elif next < x:
                start = middle
            else:
                end = middle
# @lc code=end

# print(Solution().mySqrt(6))