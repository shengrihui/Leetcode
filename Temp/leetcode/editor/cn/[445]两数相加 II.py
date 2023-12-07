# 445 两数相加 II
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        q = head
        while q:
            q = head.next
            head.next = new_head.next
            new_head.next = head
            head = q
        return new_head.next

    def addNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        r = self.addNumbers(l1, l2)
        return self.reverseList(r)
# leetcode submit region end(Prohibit modification and deletion)
