#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        l = -1
        while (s[l] != " ") and (-l <= len(s)):
            l -= 1
        return -l - 1
# @lc code=end

