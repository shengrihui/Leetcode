# 148 排序链表
# https://leetcode.cn/problems/sort-list/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = []
        p = head
        while p:
            a.append(p.val)
            p = p.next
        a.sort()
        p = head
        i = 0
        while p:
            p.val = a[i]
            i += 1
            p = p.next
        return head
# leetcode submit region end(Prohibit modification and deletion)
