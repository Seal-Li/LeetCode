#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        d = {")": "(", "]": "[", "}": "{"}
        if s[0] in d: 
            return False
        stack = []
        for bracket in s:
            if bracket in d and stack and d[bracket] == bracket:
                stack.pop()
            elif bracket in d and not stack or bracket not in d:
                stack.append(bracket)
            else:
                return False
        return not stack


# @lc code=end

