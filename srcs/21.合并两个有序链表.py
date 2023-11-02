#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = needle = ListNode(0)
        while list1 and list2:
            if list1.val >= list2.val:
                needle.next = list2
                list2 = list2.next
            else:
                needle.next = list1
                list1 = list1.next
            needle = needle.next
        if list1:
            needle.next = list1
        else:
            needle.next = list2
        return p.next
# @lc code=end

