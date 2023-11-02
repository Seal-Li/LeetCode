#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = ""
        min_len = 100000000
        for str_ in strs:
            if len(str_) < min_len:
                min_len = len(str_)
        for j in range(min_len):
            new_prefix = strs[0][:j+1]
            for str__ in strs:
                if str__[: j + 1] != new_prefix:
                    return prefix
            prefix = new_prefix
        return prefix
            
# @lc code=end

