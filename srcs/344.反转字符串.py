#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#

# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0, len(s)//2):
            tmp = s[i]
            s[i] = s[-i - 1]
            s[-i - 1] = tmp
        return s
# @lc code=end

