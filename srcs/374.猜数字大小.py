#
# @lc app=leetcode.cn id=374 lang=python3
#
# [374] 猜数字大小
#

# @lc code=start
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        left = 1
        right = n
        v = (left + right) // 2
        res = guess(v)
        while left <= right:
            if res == 1:
                left = v
                v = ceil((v + right) / 2)
            if res == -1:
                right = v
                v = floor((left + v) / 2)
            if res == 0:
                return v
            res = guess(v)
# @lc code=end

