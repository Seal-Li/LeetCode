#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
            else:
                j = j + 1
        if i == m:
            return True
        else:
            return False
# @lc code=end

