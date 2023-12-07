# 2 两数相加
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        p = ret
        c = 0
        while l1 or l2 or c:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + c
            t = ListNode(s % 10)
            c = s // 10
            p.next = t
            p = p.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ret.next
# leetcode submit region end(Prohibit modification and deletion)
