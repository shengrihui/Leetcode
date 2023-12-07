# 160 相交链表
from typing import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_list = []
        q = headA
        while q is not None:
            node_list.append(q)
            q = q.next
        q = headB
        while q is not None:
            if q in node_list:
                return q
            q = q.next
        return None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA = headB if pA == None else pA.next
            pB = headA if pB == None else pB.next
        return pA
# leetcode submit region end(Prohibit modification and deletion)
