#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1
        j = n - 1
        pos = m + n -1
        while (pos < m + n) and (i >= 0) and (j >= 0):
            if nums1[i] >= nums2[j]:
                nums1[pos] = nums1[i]
                i = i - 1
            else:
                nums1[pos] = nums2[j]
                j = j - 1
            pos = pos - 1
        if i < 0:
            for k in range(j+1):
                nums1[k] = nums2[k]
        return nums1
# @lc code=end

