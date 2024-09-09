# 2181 合并零之间的节点
# https://leetcode.cn/problems/merge-nodes-in-between-zeros/
from imports import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        ans = ListNode()
        t = ans
        while p.next:
            q = p.next
            v = 0
            while q.val != 0:
                v += q.val
                q = q.next
            s = ListNode(val=v)
            t.next = s
            t = s
            p = q
        return ans.next

# leetcode submit region end(Prohibit modification and deletion)
