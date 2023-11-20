#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        
        results = [1,1]
        for i in range(2, rowIndex+1):
            ele = [1] * (i + 1)
            for j in range(1, i):
                ele[j] = results[j-1] + results[j]
            results = ele
        return results
# @lc code=end

