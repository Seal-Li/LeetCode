#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        if m < n:
            a = "0" * (n - m) + a
        else:
            b = "0" * (m - n) + b
        
        # 用l来记录结果
        a, b = list(a), list(b)
        res = 0
        for i in range(max(n, m)-1, -1, -1):
            s = int(a[i]) + int(b[i]) + res
            if s < 2:
                a[i] = str(s)
                res = 0
            elif s == 2:
                a[i] = "0"
                res = 1
            elif s == 3:
                a[i] = "1"
                res = 1
        # 判断最后是否需要进位
        if res == 1:
            a = ["1"] + a
        return "".join(a)

# @lc code=end

