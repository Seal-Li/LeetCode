#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        results = [[1], [1,1]]
        for i in range(3, numRows+1):
            ele = [1] * i
            for j in range(1, i-1):
                ele[j] = results[i-2][j-1] + results[i-2][j]
            results.append(ele)
        return results
# @lc code=end

