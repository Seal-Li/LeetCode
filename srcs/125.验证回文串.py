#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls = []
        for ch in s:
            if ord('A') <= ord(ch) and ord(ch) <= ord('Z'):
                ls.append(chr(ord(ch) + 32))
            elif ord('a') <= ord(ch) and ord(ch) <= ord('z'):
                ls.append(ch)
            elif ord('0') <= ord(ch) and ord(ch) <= ord('9'):
                ls.append(ch)
        # print(ls)
        return ls == ls[::-1]
# @lc code=end
