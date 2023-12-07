# 25 K 个一组翻转链表
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        n = 0
        p = head
        while p is not None:
            n += 1
            p = p.next
        p = dummy  # 反转区间的前一个
        for _ in range(n // k):
            cur = p.next
            pre = p
            for i in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
            # cur 到了下一个区间的第一个
            t = p.next  # 现在 p 的 next 还是一开始区间的第一个，也就是下一个区间的前一个
            p.next.next = cur  # ，将它的 next 指向下一个区间的第一个，也就是 cur
            p.next = pre
            p = t
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
