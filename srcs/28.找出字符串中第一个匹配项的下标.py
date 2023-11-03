#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        interval = len(needle)
        for i in range(len(haystack) - interval + 1):
            if haystack[i:i+interval] == needle:
                return i
        return -1
# @lc code=end

"abcde"