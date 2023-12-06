#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = 0
        flag = True
        for chr in s:
            if flag == True and chr != " ":
                flag = False
                n += 1
            elif chr == " ":
                flag = True
        return n
                
# @lc code=end

