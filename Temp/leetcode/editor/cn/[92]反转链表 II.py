# 92 反转链表 II
from typing import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy  # 开始翻转区间的前一个
        # 让 p0 到 left 的前一个
        for _ in range(left - 1):
            p0 = p0.next

        cur = p0.next
        pre = p0
        nxt = None
        for _ in range(left, right + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        p0.next.next = cur
        p0.next = pre
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
