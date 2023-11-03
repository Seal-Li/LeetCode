#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        m = len(a) if len(a) < len(b) else len(b)
        residual= 0
        for i in range(m):
            s = int(a[-(i+1)]) + int(b[-(i+1)]) + residual
            if (s == 2):
                residual = 1
            else:
                residual = 0
                result.append[str(s)]
        
        return "".join(result[::-1])
# @lc code=end

