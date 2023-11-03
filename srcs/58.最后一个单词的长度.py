#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()[::-1]
        needle = 0
        while needle < len(s) and s[needle] != " ":
            needle += 1
        return needle
# @lc code=end