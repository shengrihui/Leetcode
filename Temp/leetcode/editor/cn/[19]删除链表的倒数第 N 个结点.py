# 19 删除链表的倒数第 N 个结点
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p = q = dummy
        for _ in range(n):
            p = p.next
        # p 先走 n 步
        # 然后两个一起走，直到 p 到了最后一个
        # q 到了要删除的前一个节点
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
