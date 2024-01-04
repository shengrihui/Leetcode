# 2487 从链表中移除节点
# https://leetcode.cn/problems/remove-nodes-from-linked-list/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        p = head
        while p :
            while p.next and p.val > p.next.val:
                p.next = p.next.next
            p = p.next
        return self.reverse(head)
# leetcode submit region end(Prohibit modification and deletion)
