#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', ']': '[', '}': '{'}
        for bracket in s:
            if bracket in ['(', '{', '[']:
                stack.append(bracket)
            else:
                if len(stack) > 0 and d[bracket] == stack[-1]:
                    stack.pop()
                else:
                    return False
            #print(stack)
        return len(stack) == 0

# @lc code=end

